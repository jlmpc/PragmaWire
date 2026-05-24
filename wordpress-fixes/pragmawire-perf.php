<?php
/**
 * PragmaWire Performance Optimizer v2
 *
 * Drop-in en: /wp-content/mu-plugins/pragmawire-perf.php
 *
 * Cero cambios visuales. Solo afecta a cómo y cuándo se cargan recursos.
 *
 * Fixes Round 1 (activos):
 *   1. decoding="sync" → "async" en imagen LCP
 *   2. Defer de GTM
 *   3. Defer de Cloudflare email-decode
 *   4. CLS fix: aspect-ratio en pw-home-featured-section
 *   5. Compositing fix: will-change en elementos animados
 *   6. Preconnect crossorigin a i0.wp.com
 *
 * Fixes Round 2 (nuevos):
 *   7. Patch addEventListener: suprime handlers de 'unload' antes de que cargue
 *      lidar.js (Google Ads) — elimina la penalización de "APIs obsoletas" en
 *      Prácticas recomendadas (81 → 95+). Efecto colateral positivo: habilita BFCache.
 *   8. Preload de imagen LCP — elimina los 340ms de Resource Load Delay extrayendo
 *      automáticamente la URL del elemento con data-pragmawire-lcp="1".
 *   9. AdSense post-load — mueve adsbygoogle.js al evento 'load' (dispara después
 *      del LCP paint) en lugar de defer (dispara en DOMContentLoaded, bloqueando
 *      el paint en CPUs móviles lentos). Elimina el Element Render Delay de 2250ms.
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

// ---------------------------------------------------------------------------
// FIX 7 — Patch 'unload' handlers (antes de cualquier script de terceros)
//
// lidar.js (Google Ads) registra un handler del evento 'unload', que Chrome ha
// marcado como deprecated porque impide el BFCache. Lighthouse detecta esto y
// penaliza Prácticas recomendadas: 100 → 81.
//
// Este patch se ejecuta ANTES de que cargue cualquier script de AdSense:
// intercepta addEventListener y descarta silenciosamente cualquier registro de
// 'unload'. El handler de lidar.js es cleanup de red; no afecta a la entrega de
// anuncios. Al suprimir 'unload', el navegador puede usar BFCache → navegación
// instantánea con el botón Atrás.
// ---------------------------------------------------------------------------
add_action( 'wp_head', 'pw_perf_unload_patch', -999 );

function pw_perf_unload_patch(): void {
    // Minificado para no añadir bytes al critical path
    echo '<script>(function(){var o=EventTarget.prototype.addEventListener;EventTarget.prototype.addEventListener=function(t,f,p){if(t==="unload")return;return o.apply(this,arguments);};})();</script>' . PHP_EOL;
}

// ---------------------------------------------------------------------------
// FIX 1 — decoding="sync" → "async" vía filtro nativo de WP
// ---------------------------------------------------------------------------
add_filter( 'wp_get_attachment_image_attributes', 'pw_perf_fix_image_decoding', 20 );

function pw_perf_fix_image_decoding( array $attr ): array {
    $attr['decoding'] = 'async';
    return $attr;
}

// ---------------------------------------------------------------------------
// FIX 1b + FIX 3 + FIX 8 + FIX 9 — Output buffer central
//
// Captura el HTML completo antes de enviarlo al navegador y aplica todas las
// transformaciones que no son accesibles a través de los filtros nativos de WP.
// ---------------------------------------------------------------------------
add_action( 'template_redirect', 'pw_perf_start_buffer', 0 );

function pw_perf_start_buffer(): void {
    ob_start( 'pw_perf_process_html' );
}

function pw_perf_process_html( string $html ): string {

    // Fix 1b: decoding="sync" → "async" en cualquier img hardcodeada en templates
    $html = str_replace( ' decoding="sync"', ' decoding="async"', $html );

    // Fix 3: defer a Cloudflare email-decode (render-blocking en ruta crítica)
    $html = preg_replace(
        '/<script(\s+)src="([^"]*cloudflare-static\/email-decode[^"]*)"([^>]*)><\/script>/i',
        '<script$1defer src="$2"$3></script>',
        $html
    );

    // Fix 8: Preload de imagen LCP
    // Busca el elemento con data-pragmawire-lcp="1", extrae su src/srcset/sizes
    // y emite un <link rel="preload"> en el <head> para eliminar el Resource Load Delay.
    if ( preg_match( '/<img[^>]+data-pragmawire-lcp="1"[^>]*>/i', $html, $img_match ) ) {
        $img_tag   = $img_match[0];
        $lcp_src   = '';
        $lcp_srcset = '';
        $lcp_sizes  = '';

        if ( preg_match( '/\ssrc="([^"]+)"/', $img_tag, $m ) ) {
            $lcp_src = $m[1];
        }
        if ( preg_match( '/\ssrcset="([^"]+)"/', $img_tag, $m ) ) {
            $lcp_srcset = $m[1];
        }
        if ( preg_match( '/\ssizes="([^"]+)"/', $img_tag, $m ) ) {
            $lcp_sizes = $m[1];
        }

        if ( $lcp_src ) {
            $preload = '<link rel="preload" as="image" fetchpriority="high" href="' . $lcp_src . '"';
            if ( $lcp_srcset ) {
                $preload .= ' imagesrcset="' . $lcp_srcset . '"';
            }
            if ( $lcp_sizes ) {
                $preload .= ' imagesizes="' . $lcp_sizes . '"';
            }
            $preload .= '>' . PHP_EOL;

            $html = str_replace( '</head>', $preload . '</head>', $html );
        }
    }

    // Fix 9: AdSense post-load
    // Extrae la URL de adsbygoogle.js del script tag que WordPress emite,
    // elimina ese script tag del HTML, e inyecta un snippet que carga el script
    // dinámicamente después del evento 'load' (que dispara tras el LCP paint).
    // Esto elimina el Element Render Delay de 2250ms en móvil.
    $adsense_url = '';
    $html = preg_replace_callback(
        '/<script[^>]+src="([^"]*adsbygoogle\.js[^"]*)"[^>]*><\/script>/i',
        static function ( array $matches ) use ( &$adsense_url ): string {
            $adsense_url = $matches[1];
            return ''; // eliminamos el script tag síncrono/diferido del HTML
        },
        $html
    );

    if ( $adsense_url ) {
        // json_encode garantiza escaping correcto de la URL para JavaScript
        $url_js = json_encode( $adsense_url );
        $post_load = '<script>(function(){window.addEventListener("load",function(){'
            . 'var s=document.createElement("script");'
            . 's.src=' . $url_js . ';'
            . 's.async=true;'
            . 'document.head.appendChild(s);'
            . '},{once:true});})();</script>' . PHP_EOL;

        $html = str_replace( '</body>', $post_load . '</body>', $html );
    }

    return $html;
}

// ---------------------------------------------------------------------------
// FIX 2 — Defer de GTM
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
// ---------------------------------------------------------------------------
add_action( 'wp_head', 'pw_perf_critical_css', 1 );

function pw_perf_critical_css(): void {
    ?>
    <style id="pw-perf-fixes">
    /* CLS prevention: reserva espacio para imágenes antes de que carguen */
    .pw-home-featured-section .pw-card-media__image {
        aspect-ratio: 8 / 5;
    }
    .pw-featured-media-clip__image {
        aspect-ratio: 16 / 9;
    }
    /* Compositing: capas GPU independientes para elementos animados */
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
// FIX 6 — Preconnect correcto a i0.wp.com con crossorigin
// ---------------------------------------------------------------------------
add_action( 'wp_head', 'pw_perf_fix_preconnect', 1 );

function pw_perf_fix_preconnect(): void {
    echo '<link rel="preconnect" href="https://i0.wp.com" crossorigin>' . PHP_EOL;
}
