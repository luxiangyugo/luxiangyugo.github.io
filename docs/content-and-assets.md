# Content and assets

## Layout

The site follows the original academic homepage structure: ordinary navigation, a short introduction with the original portrait, one news item, and selected publications. A pale gray-green background, translucent navigation and profile links, and quiet edge highlights add depth without changing the content hierarchy. Publication lists remain flat and readable. Research, the complete publication list, CV, hobbies, and contact information have separate pages. All pages are static and work without JavaScript.

The refinement draws on [Taste-Skill's redesign guidance](https://github.com/hunger-Eric/taste-skill) and [Apple-UI's material principles](https://github.com/KODxixi/Apple-UI). Their large promotional layouts, animated backgrounds, and elaborate effects are not part of this academic site. The CSS is written for this repository; no external component code or runtime was imported.

## Typography and materials

English uses the system sans-serif stack. Chinese names, navigation, and the CV introduction use [LXGW WenKai](https://github.com/lxgw/LxgwWenKai), a handwriting-like typeface, with KaiTi fallbacks. The self-hosted WOFF2 contains the site's current characters and is approximately 44 KB; it does not depend on a font CDN. The upstream font is pinned to revision `50f4b182415a8c33d9a456df220b66a284e2509b`. Its SIL Open Font License, copyright, and explicit permission for webfont subsetting are preserved in `assets/fonts/OFL-LXGW-WenKai.txt`.

After editing Chinese content, run `python scripts/subset-font.py` with `fonttools[woff]` installed, then rebuild Jekyll. The script downloads the pinned source temporarily and updates the webfont to cover characters in `_data`, `_includes`, and `_layouts`. The generated WOFF2 is committed; Pages does not need Python to build the site.

The navigation and profile links use CSS backdrop blur with a near-opaque fallback when blur is unsupported. Focus indicators, reduced-motion preferences, forced colors, and print styling are supported. Glass is limited to small surfaces so long text remains clear.

## Editing

- `_layouts/home.html`: the short homepage introduction and news placement.
- `_data/profile.yml`: public profile, Chinese introduction, links, and experience.
- `_data/research.yml`: current optical projects and all 13 entries from the previous Research page, in their original order. `method` and `result` describe technical mechanisms, supported findings, and applications without first-person contribution statements. Each project needs a figure or a video with a poster image.
- `_data/publications.yml`: published articles, full author lists, DOI links, and citations. Metadata was checked against Crossref on 14 September 2026. Selected homepage entries shorten the author list; complete authors remain on the Publications page.
- `_data/funding.yml`: NSFC Category C project 32602720, awarded and scheduled for 2027–2029.
- `_data/gallery.yml`: photographs on the Hobbies page. No dates or locations are inferred from the images.

Grade2Seg remains a research project. Optical work is described according to its current stage; ongoing research and implemented prototypes are distinguished from published papers. No experimental results are generated. The old downloadable CV is not presented as current.

## Images

The homepage uses the original `assets/img/me2.jpg` portrait. WebP derivatives of existing public repository assets are used on Research and Hobbies pages:

| Derivative | Original in assets/img |
| --- | --- |
| aerial.webp | h2_Harvest.jpg |
| botanical.webp | IMG_2323_s.jpg |
| waterfall.webp | IMG_2524_LR_s.jpg |
| landscape.webp | h3_Touring.jpg |
| portrait.webp | IMG_0602.jpg |
| cropsr.webp | r12_cropsr.png |
| grade2seg.webp | fig6_weakly_supervised.png |
| paddyseg.webp | r10_paddySeg.png |

Original assets and licensing files are preserved. The CropSR comparison figure is displayed intact.

Research includes two current optical projects followed by all 13 previous entries, retaining their original 13-to-1 numbering. All 20 original button labels and destinations are restored, including papers, repositories, datasets, videos, slides, patents, the calibration plot, poster, and thesis. The mechanism animation retains its original video and has a still-frame poster. The old `#research` anchor is preserved. The original `UnderRevision` button is retained with an explicit historical status date, not presented as a newly verified submission status.

PaddySeg and direct geo-location are separate entries as on the old page; the latter is explicitly a companion method from the same paper. Publication years follow the verified bibliography. Two compact SVG figures use archived experimental outputs for Polar–Fourier structure decomposition and Florence-2 semantic/geometry localization. Current projects share the historical entries' two-column layout, 15px body text, and short descriptions. The `full_image` field links each compact overview to its detailed plate. Mobile layouts show each title, overview, and technical description in sequence. See [technical copy sources](research-copy-sources.md) for the published results used in the summaries.

Patents are managed in `_data/patents.yml` and shown at `/patents`, after Publications in navigation. Chinese CV data is in `_data/cv_zh.yml`; the dated June 2026 source PDF is available unmodified. Contact information is consolidated into Home/CV/footer, with a short `/contact` compatibility page. See [patent and CV sources](patents-and-cv-sources.md).

See [research figure sources and generation prompts](research-figures.md) for provenance and the distinction between original research figures and generated conceptual illustrations. Sunny Optical is currently labeled as industry context; no formal collaboration, sponsorship, or product-performance claim is inferred.

## Development

Run `bundle install`, then `bundle exec jekyll serve`. Run `bundle exec jekyll build` before publishing. The Gemfile uses the GitHub Pages-compatible Jekyll 3.10 series. Keep `_site`, local dependencies, and backup clones out of the repository.

Existing paths `/research`, `/publications`, `/cv`, `/hobby`, and `/contact` are preserved. The original remote baseline is `c220b6cf7357e063525fdeb11d786d365565b9eb`. The existing Pages workflow used the `luxy-pages` branch; verify a successful deployment after pushing.
