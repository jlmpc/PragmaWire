<?php
/**
 * PragmaWire Performance Optimizer v2.1
 *
 * Drop-in en: /wp-content/mu-plugins/pragmawire-perf.php
 *
 * Parche temporal para la regresión post-WordPress 7.0.
 * Cero cambios visuales. Solo afecta a cómo y cuándo se cargan recursos.
 *
 * Mantener temporalmente mientras se integran los fixes permanentes en el tema:
 *   1. decoding="sync" -> "async" como red de seguridad.
 *   2. Defer de GTM.
 *   3. Defer de Cloudflare email-decode si Scrape Shield vuelve a activarse.
 *   4. CLS fix: aspect-ratio en pw-home-featured-section.
 *   5. Compositing fix: will-change en elementos animados.
 *   6. Preconnect crossorigin a i0.wp.com.
 *   7. Patch addEventListener: descarta handlers 'unload' de terceros.
 *   8. AdSense post-load: carga adsbygoogle.js despues del evento load.
 *
 * Importante: este MU-plugin NO genera preloads LCP. El tema 1.1.47 ya emite
 * dos preloads responsive con media queries; generar otro preload desde aqui
 * duplica la prioridad de red y puede degradar LCP.
 */

if ( ! defined( 'ABSPATH' ) ) {
	exit;
}

/**
 * Suppress third-party unload handlers before ad scripts can register them.
 */
function pw_perf_unload_patch(): void {
	echo '<script>(function(){var o=EventTarget.prototype.addEventListener;EventTarget.prototype.addEventListener=function(t,f,p){if(t==="unload")return;return o.apply(this,arguments);};})();</script>' . PHP_EOL;
}
add_action( 'wp_head', 'pw_perf_unload_patch', -999 );

/**
 * Force async decoding for attachment images as a temporary safety net.
 *
 * @param array<string,string> $attr Image attributes.
 * @return array<string,string>
 */
function pw_perf_fix_image_decoding( array $attr ): array {
	$attr['decoding'] = 'async';
	return $attr;
}
add_filter( 'wp_get_attachment_image_attributes', 'pw_perf_fix_image_decoding', 20 );

/**
 * Start final HTML buffer for transformations that cannot be handled by enqueue filters.
 */
function pw_perf_start_buffer(): void {
	if ( is_admin() || is_customize_preview() ) {
		return;
	}

	ob_start( 'pw_perf_process_html' );
}
add_action( 'template_redirect', 'pw_perf_start_buffer', 0 );

/**
 * Apply narrow public HTML performance fixes.
 *
 * @param string $html Full response HTML.
 * @return string
 */
function pw_perf_process_html( string $html ): string {
	// Hardcoded template images that bypass wp_get_attachment_image().
	$html = str_replace( ' decoding="sync"', ' decoding="async"', $html );

	// Fallback if Cloudflare Scrape Shield email obfuscation is re-enabled.
	$html = preg_replace(
		'/<script(\s+)src="([^"]*cloudflare-static\/email-decode[^"]*)"([^>]*)><\/script>/i',
		'<script$1defer src="$2"$3></script>',
		$html
	) ?? $html;

	$adsense_url = '';
	$html        = preg_replace_callback(
		'/<script[^>]+src="([^"]*adsbygoogle\.js[^"]*)"[^>]*><\/script>/i',
		static function ( array $matches ) use ( &$adsense_url ): string {
			$adsense_url = $matches[1];
			return '';
		},
		$html
	) ?? $html;

	if ( $adsense_url ) {
		$url_js    = wp_json_encode( $adsense_url );
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

/**
 * Defer GTM handles that are registered through WordPress.
 *
 * @param string $tag    Script HTML tag.
 * @param string $handle Script handle.
 * @param string $src    Script URL.
 * @return string
 */
function pw_perf_defer_third_party_scripts( string $tag, string $handle, string $src ): string {
	unset( $src );

	static $gtm_handles = [
		'google-tag-manager',
		'google-gtag',
		'gtag',
		'pw-gtm',
		'pragmawire-gtm',
	];

	if ( in_array( $handle, $gtm_handles, true ) && ! str_contains( $tag, ' defer' ) && ! str_contains( $tag, ' async' ) ) {
		$tag = str_replace( '<script ', '<script defer ', $tag );
	}

	return $tag;
}
add_filter( 'script_loader_tag', 'pw_perf_defer_third_party_scripts', 10, 3 );

/**
 * Temporary CSS safety net for CLS and compositor warnings.
 */
function pw_perf_critical_css(): void {
	?>
	<style id="pw-perf-fixes">
	.pw-home-featured-section .pw-card-media__image {
		aspect-ratio: 8 / 5;
	}
	.pw-featured-media-clip__image {
		aspect-ratio: 16 / 9;
	}
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
add_action( 'wp_head', 'pw_perf_critical_css', 1 );

/**
 * Correct preconnect for Jetpack Image CDN.
 */
function pw_perf_fix_preconnect(): void {
	echo '<link rel="preconnect" href="https://i0.wp.com" crossorigin>' . PHP_EOL;
}
add_action( 'wp_head', 'pw_perf_fix_preconnect', 1 );
