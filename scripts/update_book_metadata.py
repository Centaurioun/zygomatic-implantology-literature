#!/usr/bin/env python3
"""Utilities for synchronizing book chapter metadata and indices."""
from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import yaml


@dataclass
class BookConfig:
    key: str
    title: str
    edition: str
    editors: List[str]
    publisher: str
    publication_year: int
    doi: str
    isbn: str
    description: str
    path: Path
    bibliography: Path


BOOKS: Dict[str, BookConfig] = {
    cfg.key: cfg
    for cfg in [
        BookConfig(
            key="atlas-of-operative-oral-and-maxillofacial-surgery",
            title="Atlas of Operative Oral and Maxillofacial Surgery",
            edition="2nd",
            editors=["Christopher J. Haggerty", "Robert M. Laughlin"],
            publisher="Wiley-Blackwell",
            publication_year=2023,
            doi="10.1002/9781119683957",
            isbn="9781119683957",
            description="Comprehensive surgical atlas with operative workflows, grafting, trauma, and reconstruction techniques.",
            path=Path("books/atlas-of-operative-oral-and-maxillofacial-surgery"),
            bibliography=Path("bibliography/atlas-of-operative-oral-and-maxillofacial-surgery.md"),
        ),
        BookConfig(
            key="petersons-principles-of-oral-and-maxillofacial-surgery",
            title="Peterson's Principles of Oral and Maxillofacial Surgery",
            edition="2022 edition",
            editors=["Michael Miloro", "G. E. Ghali", "Peter E. Larsen", "Peter Waite"],
            publisher="Springer International Publishing",
            publication_year=2022,
            doi="10.1007/978-3-030-91920-7",
            isbn="9783030919207",
            description="Reference text covering core OMFS diagnostics, orthognathic planning, trauma management, and reconstructive care.",
            path=Path("books/petersons-principles-of-oral-and-maxillofacial-surgery"),
            bibliography=Path("bibliography/petersons-principles-of-oral-and-maxillofacial-surgery.md"),
        ),
        BookConfig(
            key="advances-in-dental-implantology-using-nanomaterials-and-allied-technology-applications",
            title="Advances in Dental Implantology Using Nanomaterials and Allied Technology Applications",
            edition="1st",
            editors=["R. S. Chaughule", "Rajesh Dashaputra"],
            publisher="Springer International Publishing",
            publication_year=2021,
            doi="10.1007/978-3-030-52207-0",
            isbn="9783030522070",
            description="Nanomaterials-focused implantology monograph covering biomaterials, CAD/CAM workflows, and reconstructive innovations.",
            path=Path("books/advances-in-dental-implantology-using-nanomaterials-and-allied-technology-applications"),
            bibliography=Path("bibliography/advances-in-dental-implantology.md"),
        ),
    ]
}


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    value = value.replace("'", "").replace("`", "")
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value)
    return value.strip("-").lower()


def normalize_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").lower()
    return normalized.replace("'", "")


def parse_authors(raw: str) -> List[str]:
    cleaned = raw.replace(" & ", ", ").replace(" and ", ", ")
    parts = [p.strip() for p in cleaned.split(",") if p.strip()]
    authors: List[str] = []
    i = 0
    while i < len(parts):
        last = parts[i]
        initials = parts[i + 1] if i + 1 < len(parts) else ""
        author = f"{last}, {initials}".strip().strip(",")
        authors.append(author)
        i += 2
    return authors


def parse_bibliography(path: Path, book_title: str) -> Dict[str, Dict[str, str]]:
    if not path.exists():
        return {}
    target = normalize_text(book_title)
    lines = [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    meta: Dict[str, Dict[str, str]] = {}
    pattern = re.compile(r"(?P<authors>.+?) \((?P<year>\d{4})(?P<suffix>[a-z])?\)\. (?P<title>.+?)\. In (?P<rest>.+)")
    for line in lines:
        if ". In " not in line or target not in normalize_text(line):
            continue
        match = pattern.match(line)
        if not match:
            continue
        authors = parse_authors(match.group("authors"))
        year = int(match.group("year"))
        title = match.group("title").strip()
        try:
            _, doi = match.group("rest").strip().rsplit(". ", 1)
        except ValueError:
            doi = ""
        pages_match = re.search(r"pp\\.\\s*([^).]+)", line)
        pages = pages_match.group(1).strip() if pages_match else ""
        first_author = authors[0] if authors else ""
        first_last = first_author.split(",")[0] if first_author else title.split()[0]
        slug = slugify(f"{first_last}-{year}-{title}")
        meta[slug] = {
            "title": title,
            "authors": authors,
            "year": year,
            "pages": pages,
            "doi": doi.rstrip(".").strip(),
        }
    return meta


def update_front_matter(md_path: Path, cfg: BookConfig, meta: Dict[str, str]) -> None:
    text = md_path.read_text(encoding="utf-8")
    if text.startswith("---"):
        _, front, body = text.split("---", 2)
        data = yaml.safe_load(front) or {}
    else:
        data = {}
        body = text
    changed = False

    def setdefault(key: str, value):
        nonlocal changed
        if value in (None, ""):
            return
        if key not in data:
            data[key] = value
            changed = True

    setdefault("title", meta.get("title"))
    setdefault("authors", meta.get("authors"))
    setdefault("year", meta.get("year"))
    setdefault("pages", meta.get("pages"))
    setdefault("chapter_doi", meta.get("doi"))
    setdefault("source_file", md_path.name)

    for key, value in (
        ("book_title", cfg.title),
        ("book_editors", cfg.editors),
        ("book_publisher", cfg.publisher),
        ("book_doi", cfg.doi),
        ("book_isbn", cfg.isbn),
        ("publication_year", meta.get("year", cfg.publication_year)),
    ):
        if data.get(key) != value and value not in (None, ""):
            data[key] = value
            changed = True

    if changed or not text.startswith("---"):
        front = "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True) + "---\n"
        md_path.write_text(front + body.lstrip("\n"), encoding="utf-8")


def ensure_book_metadata(cfg: BookConfig) -> None:
    chapters_dir = cfg.path / "chapters"
    bibliography = parse_bibliography(cfg.bibliography, cfg.title)
    for entry in sorted(os.listdir(chapters_dir)):
        entry_path = chapters_dir / entry
        if entry_path.is_dir():
            md_files = [entry_path / f for f in os.listdir(entry_path) if f.endswith(".md")]
        elif entry_path.suffix == ".md":
            md_files = [entry_path]
        else:
            continue
        for md_path in md_files:
            slug = md_path.stem
            meta = bibliography.get(slug)
            if not meta:
                for key, value in bibliography.items():
                    if slug.startswith(key) or key.startswith(slug) or key in slug or slug in key:
                        meta = value
                        break
            if meta:
                update_front_matter(md_path, cfg, meta)

    generate_book_assets(cfg)


def generate_book_assets(cfg: BookConfig) -> None:
    chapters_dir = cfg.path / "chapters"
    records = []
    for root, _, files in os.walk(chapters_dir):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            path = Path(root) / fname
            rel_path = path.relative_to(cfg.path)
            front = path.read_text(encoding="utf-8").split("---", 2)[1]
            data = yaml.safe_load(front) or {}
            title = data.get("title", rel_path.stem.replace("-", " ").title())
            authors = data.get("authors", [])
            if isinstance(authors, list):
                author_str = "; ".join(authors)
            else:
                author_str = str(authors)
            records.append({
                "title": title,
                "authors": author_str,
                "pages": data.get("pages", ""),
                "doi": data.get("chapter_doi") or data.get("doi") or data.get("url"),
                "path": rel_path.as_posix(),
            })
    records.sort(key=lambda r: r["title"])

    metadata = {
        "title": cfg.title,
        "edition": cfg.edition,
        "editors": cfg.editors,
        "publisher": cfg.publisher,
        "publication_year": cfg.publication_year,
        "doi": cfg.doi,
        "isbn": cfg.isbn,
        "chapter_count": len(records),
        "description": cfg.description,
    }
    (cfg.path / "metadata.yaml").write_text(yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True), encoding="utf-8")

    readme_lines = [
        f"# {cfg.title}",
        cfg.description,
        "## Book Details",
        f"- **Edition:** {cfg.edition}",
        f"- **Editors:** {', '.join(cfg.editors)}",
        f"- **Publisher:** {cfg.publisher} ({cfg.publication_year})",
        f"- **DOI:** {cfg.doi}",
        f"- **ISBN:** {cfg.isbn}",
        f"- **Chapters:** {len(records)} files",
        "",
        "## Chapter Index",
        "| Chapter | Authors | Pages | DOI | File |",
        "| --- | --- | --- | --- | --- |",
    ]
    for record in records:
        doi_link = f"[{record['doi']}]({record['doi']})" if record['doi'] else ""
        file_link = f"[{record['path']}]({record['path']})"
        readme_lines.append(f"| {record['title']} | {record['authors']} | {record['pages']} | {doi_link} | {file_link} |")
    (cfg.path / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")


def generate_publications_readme() -> None:
    pub_dir = Path("publications")
    articles = sorted(pub_dir.glob("*.md"))
    years: Dict[int, int] = {}
    for path in articles:
        content = path.read_text(encoding="utf-8")
        segments = content.split("---", 2)
        if len(segments) < 3:
            # Skip helper files (e.g., README.md) that intentionally omit front matter.
            continue
        front = segments[1]
        data = yaml.safe_load(front) or {}
        year = data.get("year")
        if isinstance(year, int):
            years[year] = years.get(year, 0) + 1
    lines = [
        "# Publications",
        f"- Curated Markdown articles: **{len(articles)}**",
        "- Each file begins with YAML front matter capturing bibliographic metadata (title, authors, journal, year, DOI, etc.).",
        "- Use `rg` or other tooling against the front matter to build custom bibliographies.",
        "",
        "## Quick Stats",
    ]
    for year in sorted(years):
        lines.append(f"- {year}: {years[year]} files")
    lines.extend([
        "",
        "## Usage",
        '- Search by topic: `rg -l "zygoma" publications`',
        '- Extract metadata: `rg -n "^title" publications/example.md`',
    ])
    pub_dir.joinpath("README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for cfg in BOOKS.values():
        ensure_book_metadata(cfg)
    generate_publications_readme()


if __name__ == "__main__":
    main()
