"""Build the site's Chinese webfont. Requires fonttools[woff] (pip install).

Usage: python scripts/subset-font.py [path/to/LXGWWenKai-Regular.ttf]
Without a font path, downloads the pinned upstream font into a temporary folder.
"""
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve
import sys

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
REVISION = "50f4b182415a8c33d9a456df220b66a284e2509b"
UPSTREAM = f"https://raw.githubusercontent.com/lxgw/LxgwWenKai/{REVISION}"
DESTINATION = ROOT / "assets/fonts"


def build(source):
    text = "".join(
        path.read_text(encoding="utf-8")
        for folder in ("_data", "_includes", "_layouts")
        for path in (ROOT / folder).rglob("*")
        if path.suffix in (".html", ".yml")
    )
    characters = {ord(c) for c in text if ord(c) > 127} | set(range(32, 127))
    font = TTFont(source)
    missing = characters - font.getBestCmap().keys()
    if missing:
        raise ValueError(f"Source font is missing characters: {sorted(missing)}")
    options = subset.Options()
    options.flavor = "woff2"
    options.name_IDs = [0, 1, 2, 3, 4, 5, 6, 13, 14]
    options.name_legacy = True
    subsetter = subset.Subsetter(options=options)
    subsetter.populate(unicodes=characters)
    subsetter.subset(font)
    font.flavor = "woff2"
    target = DESTINATION / "lxgw-wenkai-site.woff2"
    font.save(target)
    print(f"Built {target.name}: {len(characters)} characters, {target.stat().st_size:,} bytes")


if __name__ == "__main__":
    DESTINATION.mkdir(parents=True, exist_ok=True)
    license_path = DESTINATION / "OFL-LXGW-WenKai.txt"
    urlretrieve(f"{UPSTREAM}/OFL.txt", license_path)
    license_text = "\n".join(line.rstrip() for line in license_path.read_text(encoding="utf-8").splitlines()) + "\n"
    license_path.write_bytes(license_text.encode("utf-8"))
    if len(sys.argv) > 1:
        build(Path(sys.argv[1]))
    else:
        with TemporaryDirectory(prefix="homepage-font-") as temporary:
            source = Path(temporary) / "LXGWWenKai-Regular.ttf"
            urlretrieve(f"{UPSTREAM}/fonts/TTF/LXGWWenKai-Regular.ttf", source)
            build(source)
