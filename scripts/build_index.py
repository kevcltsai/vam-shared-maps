#!/usr/bin/env python3
"""Generate index.html from maps/*.html.

- Title: maps.json "title" override, else the file's <title>, else the file name.
- Category / description: optional, from maps.json. Maps not listed there go
  under "其他", so a new map shows up on the homepage even if you forget
  to edit maps.json.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAPS_DIR = ROOT / "maps"
CATALOG = ROOT / "maps.json"
OUT = ROOT / "index.html"
FALLBACK_CATEGORY = "其他"
TITLE_RE = re.compile(rb"<title>(.*?)</title>", re.I | re.S)


def read_title(path: Path) -> str:
    # Exported maps can be several MB; <title> is in <head>, so the start is enough.
    with path.open("rb") as f:
        head = f.read(256 * 1024)
    m = TITLE_RE.search(head)
    if m:
        title = html.unescape(m.group(1).decode("utf-8", "replace")).strip()
        if title:
            return title
    return path.stem


def main() -> None:
    catalog = json.loads(CATALOG.read_text("utf-8")) if CATALOG.exists() else {}
    meta = catalog.get("maps", {})
    order = list(catalog.get("categories", []))

    groups: dict[str, list[tuple[str, str, str]]] = {}
    # Listed maps keep maps.json order; unlisted ones follow, by file name.
    listed = list(meta)
    paths = sorted(MAPS_DIR.glob("*.html"),
                   key=lambda p: (listed.index(p.name) if p.name in listed else len(listed), p.name))
    for path in paths:
        info = meta.get(path.name, {})
        title = info.get("title") or read_title(path)
        cat = info.get("category") or FALLBACK_CATEGORY
        groups.setdefault(cat, []).append((path.name, title, info.get("description", "")))
        if cat not in order:
            order.append(cat)

    sections = []
    for cat in order:
        items = groups.get(cat)
        if not items:
            continue
        lis = []
        for name, title, desc in items:
            line = f'    <li><a href="maps/{html.escape(name)}">{html.escape(title)}</a>'
            if desc:
                line += f"：{html.escape(desc)}"
            lis.append(line + "</li>")
        sections.append(f"  <h2>{html.escape(cat)}</h2>\n  <ul>\n" + "\n".join(lis) + "\n  </ul>")

    page = f"""<!doctype html>
<!-- 這個檔案由 scripts/build_index.py 自動產生，請勿手動修改；分類與說明改 maps.json。 -->
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>VAM 分享地圖</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: system-ui, -apple-system, "PingFang TC", sans-serif; max-width: 640px; margin: 48px auto; padding: 0 16px; line-height: 1.7; }}
  a {{ color: #5b5bd6; }}
  h2 {{ font-size: 1.1em; margin-top: 28px; }}
  li {{ margin: 6px 0; }}
</style>
</head>
<body>
  <h1>VAM 分享地圖</h1>
  <p>用 Visual Agent Map 整理的心智圖。點一張地圖開啟，可以拖曳、縮放、點議題看內容。</p>

{(chr(10) * 2).join(sections)}
</body>
</html>
"""
    OUT.write_text(page, "utf-8")
    print(f"wrote {OUT.name}: {sum(len(v) for v in groups.values())} maps")


if __name__ == "__main__":
    main()
