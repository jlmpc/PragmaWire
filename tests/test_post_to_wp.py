from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "post_to_wp.py"
SPEC = importlib.util.spec_from_file_location("post_to_wp", SCRIPT)
post_to_wp = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(post_to_wp)


VALIDATED_ARTICLE = """ESTADO_SUPERVISION_FINAL:
CREAR_WORDPRESS_DRAFT

WORDPRESS_DRAFT_VALIDADO:
title: Test completo de metadata
slug: test-completo-metadata
excerpt: Extracto visible para WordPress y resultados de búsqueda.
category_primary: Seguridad Digital
category_secondary:
tags: passkeys, seguridad digital, gestores de contraseñas
meta_title: Test metadata WordPress | PragmaWire
meta_description: Extracto SEO para validar Jetpack y el campo avanzado de descripción.
focus_keyword: seguridad digital
secondary_keywords:
- passkeys
- gestores de contraseñas
search_intent: informational
content_type: guía
ai_summary: Resumen corto para motores de IA.
quotable_sentence: Una frase citable de prueba.
main_entities:
- WordPress
- Jetpack
- PragmaWire
internal_links_suggested:
- Guía sobre passkeys
external_sources_recommended:
- Fuente: INCIBE
  Tipo: organismo
  Respalda: seguridad digital
  Estado: pendiente
update_level: medio
obsolescence_risk: medio
suggested_featured_image:
  description: Imagen manual para generar después.
  style: editorial tecnológico
  elements: móvil, candado, interfaz
  alt_text: Usuario revisando seguridad digital en el móvil

ARTICLE_MARKDOWN:
# Test completo de metadata

Introducción del artículo.

## Sección interna

Contenido que no debe cortarse.

FAQ_SCHEMA_CANDIDATES:
1. Pregunta:
   Respuesta:

NOTAS_PARA_REVISION_HUMANA:
- Revisar antes de publicar.
"""


class PostToWpTest(unittest.TestCase):
    def article_file(self, text: str = VALIDATED_ARTICLE) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        path = Path(tmp.name) / "articulo_001_wordpress_ready.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_parse_validated_wordpress_draft(self) -> None:
        article = post_to_wp.parse_article(self.article_file())

        self.assertEqual(article["title"], "Test completo de metadata")
        self.assertEqual(article["slug"], "test-completo-metadata")
        self.assertEqual(article["category_primary"], "Seguridad Digital")
        self.assertEqual(article["tags"], ["passkeys", "seguridad digital", "gestores de contraseñas"])
        self.assertEqual(article["meta_title"], "Test metadata WordPress | PragmaWire")
        self.assertIn("Contenido que no debe cortarse", article["article_markdown"])
        self.assertIn("Imagen destacada sugerida", article["article_markdown"])

    def test_preview_payload_contains_wordpress_metadata(self) -> None:
        article = post_to_wp.parse_article(self.article_file())
        preview = post_to_wp.preview_payload(article)

        self.assertEqual(preview["category_ids"], [14])
        self.assertEqual(preview["tags"], ["passkeys", "seguridad digital", "gestores de contraseñas"])
        self.assertEqual(preview["meta"]["jetpack_seo_html_title"], "Test metadata WordPress | PragmaWire")
        self.assertEqual(
            preview["meta"]["advanced_seo_description"],
            "Extracto SEO para validar Jetpack y el campo avanzado de descripción.",
        )
        self.assertFalse(preview["meta"]["jetpack_seo_noindex"])
        self.assertFalse(preview["meta"]["jetpack_publicize_feature_enabled"])

    def test_missing_required_metadata_blocks_article(self) -> None:
        broken = VALIDATED_ARTICLE.replace("meta_description: Extracto SEO para validar Jetpack y el campo avanzado de descripción.\n", "")
        with self.assertRaises(post_to_wp.PublishError):
            post_to_wp.parse_article(self.article_file(broken))


if __name__ == "__main__":
    unittest.main()
