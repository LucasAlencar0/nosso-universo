"""Gera o index.html do site (GitHub Pages) a partir do laura.html.

Uso:  python build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
"""

body = (ROOT / "laura.html").read_text(encoding="utf-8")
(ROOT / "index.html").write_text(HEAD + body + "\n</html>\n", encoding="utf-8")
print("index.html gerado")
