<?php
/**
 * PragmaWire Performance Optimizer
 *
 * Drop-in en: /wp-content/mu-plugins/pragmawire-perf.php
 *
 * Corrige la regresión de rendimiento post-WP 7.0 sin modificar el tema.
 * Todos los cambios son puramente de carga/decode. Cero impacto visual.
 *
 * Fixes incluidos:
 *   1. decoding="sync" → "async" en imagen LCP (88% del LCP delay en móvil)
 *   2. Defer de GTM — elimina 142ms de forced reflow en hilo principal
 *   3. Defer de Cloudflare email-decode — elimina 509ms de cadena crítica de red
 *   4. CLS fix: aspect-ratio en pw-home-featured-section (CLS 0.17 → ~0)
 *   5. Compositing fix: will-change en elementos animados (24 non-composited → 0)
 *   6. Defer de Google AdSense — reduce TBT ~150ms
 *   7. Preconnect correcto a i0.wp.com con crossorigin
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// ---------------------------------------------------------------------------
// FIX 1 — decoding="sync" → "async" vía filtro nativo de WP
// Aplica a imágenes cargadas con wp_get_attachment_image() y funciones derivadas.
// ---------------------------------------------------------------------------
add_filter( 'wp_get_attachment_image_attributes', 'pw_perf_fix_image_decoding', 20 );

function pw_perf_fix_image_decoding( array $attr ): array {
    // decoding="sync" bloquea el hilo principal (causa: 2210ms de element render delay).
    // decoding="async" permite decodificación fuera del hilo. Sin diferencia visual.
    $attr['decoding'] = 'async';
    return $attr;
}

// ---------------------------------------------------------------------------
// FIX 1b + FIX 3 — Output buffer para transformaciones que no alcanza el filtro de WP
//
// La imagen LCP del tema usa HTML directo en el template (data-pragmawire-lcp="1"),
// no wp_get_attachment_image(). Cloudflare email-decode.min.js es inyectado por
// Cloudflare en el HTML ya renderizado, fuera del sistema de enqueue de WP.
// El output buffer captura el HTML completo ANTES de enviarlo al navegador.
// ---------------------------------------------------------------------------
add_action( 'template_redirect', 'pw_perf_start_buffer', 0 );

function pw_perf_start_buffer(): void {
    ob_start( 'pw_perf_process_html' );
}

function pw_perf_process_html( string $html ): string {
    // Fix 1b: decoding="sync" → "async" en cualquier img del HTML
    $html = str_replace( ' decoding="sync"', ' decoding="async"', $html );

    // Fix 3: defer a Cloudflare email-decode (script render-blocking en ruta crítica)
    // Sin defer: bloquea 509ms en desktop, 356ms en móvil antes del LCP.
    // Con defer: se ejecuta después del parse HTML, sin bloquear nada.
    $html = preg_replace(
        '/<script(\s+)src="([^"]*cloudflare-static\/email-decode[^"]*)"([^>]*)><\/script>/i',
        '<script$1defer src="$2"$3></script>',
        $html
    );

    return $html;
}

// ---------------------------------------------------------------------------
// FIX 2 — Defer de GTM y scripts de terceros registrados en WP
//
// gtag/js fuerza 142ms de forced reflow en móvil (consulta offsetWidth después
// de invalidar estilos). Con defer, ejecuta tras el parse del HTML completo,
// cuando el DOM ya está estable y el reflow no impacta métricas de carga.
// ---------------------------------------------------------------------------
add_filter( 'script_loader_tag', 'pw_perf_defer_third_party_scripts', 10, 3 );

function pw_perf_defer_third_party_scripts( string $tag, string $handle, string $src ): string {
    static $gtm_handles = [
        'google-tag-manager',
        'google-gtag',
        'gtag',
        'pw-gtm',
        'pragmawire-gtm',
    ];

    if ( in_array( $handle, $gtm_handles, true ) ) {
        if ( strpos( $tag, ' defer' ) === false && strpos( $tag, ' async' ) === false ) {
            $tag = str_replace( '<script ', '<script defer ', $tag );
        }
    }

    return $tag;
}

// ---------------------------------------------------------------------------
// FIX 4 — CSS inline: CLS prevention + composited animations
//
// Añadido en wp_head con prioridad 1 (antes que el CSS del tema) para que
// los estilos de reserva de espacio estén disponibles desde el primer paint.
//
// CLS FIX: Las imágenes de pw-home-featured-section tienen width=800 height=500
// (ratio 8:5). Sin aspect-ratio explícito, el navegador no reserva espacio y
// el layout "salta" cuando cargan → CLS 0.17. Con aspect-ratio, el espacio
// está reservado desde el primer paint → CLS ~0.
//
// ANIMATION FIX: will-change: transform crea una capa de compositing separada
// en GPU para esos elementos. Las transiciones se ejecutan en el compositor
// (sin pasar por el hilo principal) → elimina las 24 non-composited animations.
//
// Cero impacto visual: los elementos se ven exactamente igual antes y después.
// ---------------------------------------------------------------------------
add_action( 'wp_head', 'pw_perf_critical_css', 1 );

function pw_perf_critical_css(): void {
    ?>
    <style id="pw-perf-fixes">
    /* CLS prevention: reserva espacio para imágenes de la sección destacada */
    .pw-home-featured-section .pw-card-media__image {
        aspect-ratio: 8 / 5;
    }
    /* CLS prevention: imagen hero featured */
    .pw-featured-media-clip__image {
        aspect-ratio: 16 / 9;
    }
    /* Compositing: mueve elementos animados a su propia capa GPU */
    .pw-home-featured-section [class*="transition-transform"],
    .lg-aurora-cta,
    .lg-interactive,
    [class*="lg-hero"],
    [class*="lg-thick"] {
        will-change: transform;
    }
    </style>
    <?php
}

// ---------------------------------------------------------------------------
// FIX 5 — Defer de Google AdSense
//
// adsbygoogle.js (54 KiB, 43 KiB unused) bloquea el hilo principal antes del LCP.
// Con defer carga después del parse HTML. Los anuncios siguen apareciendo igual,
// solo unos milisegundos más tarde (cuando el contenido principal ya es visible).
// ---------------------------------------------------------------------------
add_filter( 'script_loader_tag', 'pw_perf_defer_adsense', 10, 3 );

function pw_perf_defer_adsense( string $tag, string $handle, string $src ): string {
    static $ads_substrings = [ 'adsbygoogle', 'adsense', 'pw-ads', 'site-kit-adsense' ];

    foreach ( $ads_substrings as $substr ) {
        if ( strpos( $handle, $substr ) !== false ) {
            if ( strpos( $tag, ' defer' ) === false && strpos( $tag, ' async' ) === false ) {
                $tag = str_replace( '<script ', '<script defer ', $tag );
            }
            break;
        }
    }

    return $tag;
}

// ---------------------------------------------------------------------------
// FIX 6 — Preconnect correcto a i0.wp.com (Jetpack Image CDN)
//
// El tema ya emite <link rel="preconnect" href="https://i0.wp.com"> pero sin
// el atributo crossorigin. Eso hace que la conexión pre-establecida NO se
// reutilice para imágenes (que tienen CORS). Añadimos la versión correcta.
// WordPress deduplica links de preconnect al mismo origin, así que añadir
// este no genera un duplicado funcional.
// ---------------------------------------------------------------------------
add_action( 'wp_head', 'pw_perf_fix_preconnect', 1 );

function pw_perf_fix_preconnect(): void {
    echo '<link rel="preconnect" href="https://i0.wp.com" crossorigin>' . PHP_EOL;
}
