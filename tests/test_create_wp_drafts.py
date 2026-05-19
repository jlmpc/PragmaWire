from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "create_wp_drafts.py"
SPEC = importlib.util.spec_from_file_location("create_wp_drafts", SCRIPT)
create_wp_drafts = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(create_wp_drafts)


READY_ARTICLE = """ESTADO_SUPERVISION_FINAL: CREAR_WORDPRESS_DRAFT

## WORDPRESS_DRAFT_VALIDADO

TITULO: Test de metadata completa
SLUG: test-metadata-completa
META_TITLE: Test SEO Title | PragmaWire
META_DESCRIPTION: Extracto SEO de prueba para comprobar que WordPress recibe el campo correcto.
CATEGORY: Seguridad Digital
TAGS: seguridad digital, contraseñas, passkeys
STATUS: draft
FOCUS_KEYWORD: seguridad digital
SECONDARY_KEYWORDS: contraseñas seguras, passkeys
SEARCH_INTENT: informational
CONTENT_TYPE: guía práctica
AI_SUMMARY: Resumen IA de prueba.
QUOTABLE_SENTENCE: Frase citable de prueba.
MAIN_ENTITIES: PragmaWire, WordPress, Jetpack
INTERNAL_LINKS: /que-son-passkeys/
UPDATE_LEVEL: semestral
OBSOLESCENCE_RISK: MEDIO
FEATURED_IMAGE_DESCRIPTION: Descripción manual de imagen.
FEATURED_IMAGE_ALT: Alt manual de imagen.
FAQ_SCHEMA_CANDIDATES:
  - Q: ¿Pregunta uno?
    A: Respuesta uno.
  - Q: ¿Pregunta dos?
    A: Respuesta dos.

---

## NOTAS_PARA_REVISION_HUMANA

- Revisar imagen.
"""

EDITED_ARTICLE = """## ARTICULO_FINAL_MARKDOWN

# Test de metadata completa

Contenido del artículo final.

## Subtítulo interno

Este bloque no debe perderse al extraer el cuerpo.

## NOTAS_EDITOR_FINAL

OK
"""


class CreateWpDraftsTest(unittest.TestCase):
    def make_run(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        run_path = Path(tmp.name) / "run"
        (run_path / "05-wordpress-ready").mkdir(parents=True)
        (run_path / "04-edited").mkdir(parents=True)
        (run_path / "05-wordpress-ready" / "_STAGE_COMPLETE").write_text("", encoding="utf-8")
        (run_path / "05-wordpress-ready" / "articulo_001_wordpress_ready.md").write_text(READY_ARTICLE, encoding="utf-8")
        (run_path / "04-edited" / "articulo_001_edited.md").write_text(EDITED_ARTICLE, encoding="utf-8")
        return run_path

    def test_parser_extracts_required_metadata(self) -> None:
        run_path = self.make_run()
        article = create_wp_drafts.load_articles(run_path)[0]

        self.assertEqual(article["fields"]["SLUG"], "test-metadata-completa")
        self.assertEqual(article["category_id"], 14)
        self.assertEqual(article["tag_names"], ["seguridad digital", "contraseñas", "passkeys"])
        self.assertEqual(len(article["faq_schema_candidates"]), 2)
        self.assertIn("Contenido del artículo final", article["content"])
        self.assertIn("Este bloque no debe perderse", article["content"])

    def test_payload_contains_wordpress_and_jetpack_metadata(self) -> None:
        run_path = self.make_run()
        article = create_wp_drafts.load_articles(run_path)[0]
        payload = create_wp_drafts.build_payload(article, tag_ids=[101, 102, 103])

        self.assertEqual(payload["slug"], "test-metadata-completa")
        self.assertEqual(payload["excerpt"], article["fields"]["META_DESCRIPTION"])
        self.assertEqual(payload["categories"], [14])
        self.assertEqual(payload["tags"], [101, 102, 103])
        self.assertEqual(payload["meta"]["jetpack_seo_html_title"], "Test SEO Title | PragmaWire")
        self.assertEqual(payload["meta"]["advanced_seo_description"], article["fields"]["META_DESCRIPTION"])
        self.assertFalse(payload["meta"]["jetpack_seo_noindex"])
        self.assertFalse(payload["meta"]["jetpack_publicize_feature_enabled"])
        self.assertNotIn("featured_media", payload)

    def test_preview_contains_payload_template_for_dry_run_review(self) -> None:
        run_path = self.make_run()
        article = create_wp_drafts.load_articles(run_path)[0]
        preview = create_wp_drafts.make_preview([article])
        item = preview["articles"][0]

        self.assertEqual(item["payload_template"]["categories"], [14])
        self.assertEqual(item["payload_template"]["tags"], [])
        self.assertEqual(item["payload_template"]["meta"]["jetpack_seo_html_title"], "Test SEO Title | PragmaWire")
        self.assertEqual(item["tag_resolution"], "resolved_or_created_at_publish_time")

    def test_missing_required_metadata_blocks_article(self) -> None:
        run_path = self.make_run()
        ready_path = run_path / "05-wordpress-ready" / "articulo_001_wordpress_ready.md"
        ready_path.write_text(READY_ARTICLE.replace("META_DESCRIPTION: Extracto SEO de prueba para comprobar que WordPress recibe el campo correcto.\n", ""), encoding="utf-8")

        with self.assertRaises(create_wp_drafts.PublishError) as ctx:
            create_wp_drafts.load_articles(run_path)

        self.assertIn("META_DESCRIPTION", str(ctx.exception))

    def test_all_pipeline_categories_resolve_to_wordpress_ids(self) -> None:
        expected = {
            "Hogar Inteligente": 16,
            "Hogar inteligente": 16,
            "Inteligencia Artificial": 13,
            "Productividad Digital": 15,
            "Recomendaciones Tecnológicas": 5,
            "Salud y Bienestar": 18,
            "Salud y Bienestar Digital": 18,
            "Seguridad Digital": 14,
        }

        for name, category_id in expected.items():
            with self.subTest(name=name):
                self.assertEqual(create_wp_drafts.category_id(name), category_id)

    def test_featured_media_id_is_only_sent_when_numeric_id_exists(self) -> None:
        run_path = self.make_run()
        ready_path = run_path / "05-wordpress-ready" / "articulo_001_wordpress_ready.md"
        ready_path.write_text(READY_ARTICLE.replace("FEATURED_IMAGE_ALT:", "FEATURED_MEDIA_ID: 321\nFEATURED_IMAGE_ALT:"), encoding="utf-8")

        article = create_wp_drafts.load_articles(run_path)[0]
        payload = create_wp_drafts.build_payload(article, tag_ids=[101])

        self.assertEqual(payload["featured_media"], 321)

    def test_confirmation_requires_exact_metadata(self) -> None:
        run_path = self.make_run()
        article = create_wp_drafts.load_articles(run_path)[0]
        post = {
            "slug": "test-metadata-completa",
            "excerpt": {"raw": article["fields"]["META_DESCRIPTION"]},
            "categories": [14],
            "tags": [101, 102],
            "meta": {
                "jetpack_seo_html_title": "Test SEO Title | PragmaWire",
                "advanced_seo_description": article["fields"]["META_DESCRIPTION"],
                "jetpack_seo_noindex": False,
            },
        }

        ok = create_wp_drafts.confirm_post(post, article, [101, 102])
        self.assertTrue(ok["ok"])

        post["meta"]["advanced_seo_description"] = "otra"
        failed = create_wp_drafts.confirm_post(post, article, [101, 102])
        self.assertFalse(failed["ok"])
        self.assertFalse(failed["checks"]["seo_description"])


if __name__ == "__main__":
    unittest.main()
