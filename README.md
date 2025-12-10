# Knowledgebase for Zygomatic Implantology and Maxillofacial Surgery Literature

This repository consolidates a curated collection of 247 standalone articles and three book collections related to zygomatic implantology and maxillofacial surgery. Each publication is stored as a Markdown file with standardized YAML front matter for easy metadata extraction and programmatic access.

## Structure
- `publications/` – 247 standalone articles with standardized front matter and a usage guide.
- `books/` – Three organized book collections (`atlas`, `Peterson's Principles`, `Advances in Dental Implantology`) with chapter-level metadata, per-book `README.md`, and `metadata.yaml` files.
- `scripts/` – ETL scripts for metadata extraction, validation, and corpus management.

## Working With the Library
1. Use `rg` or your preferred toolkit against the YAML front matter to filter by title, DOI, or publication year.
2. Book chapters already include `book_*` keys so you can render per-book catalogs or cite sections programmatically.
3. Run `python scripts/update_book_metadata.py` whenever bibliographies change; it updates chapter front matter, regenerates `metadata.yaml`, and rebuilds the chapter indices.

## Next Steps
- Wire this repository to a Git remote (see instructions below) to collaborate with version control.
- Extend `scripts/` with additional ETL tasks (e.g., DOI validation or PDF synchronization) as the corpus grows.
