# Content and assets

## Layout

The site follows the original academic homepage structure: white background, ordinary navigation, a short introduction with the original portrait, one news item, and selected publications. Research, the complete publication list, CV, hobbies, and contact information have separate pages. All pages are static and work without JavaScript.

## Editing

- `_layouts/home.html`: the short homepage introduction and news placement.
- `_data/profile.yml`: public profile, Chinese introduction, links, and experience.
- `_data/research.yml`: project descriptions and their current status.
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

## Development

Run `bundle install`, then `bundle exec jekyll serve`. Run `bundle exec jekyll build` before publishing. The Gemfile uses the GitHub Pages-compatible Jekyll 3.10 series. Keep `_site`, local dependencies, and backup clones out of the repository.

Existing paths `/research`, `/publications`, `/cv`, `/hobby`, and `/contact` are preserved. The original remote baseline is `c220b6cf7357e063525fdeb11d786d365565b9eb`. The existing Pages workflow used the `luxy-pages` branch; verify a successful deployment after pushing.
