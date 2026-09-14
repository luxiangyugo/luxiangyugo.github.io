# Content and assets

Updated 14 September 2026. The website is a Jekyll site and deploys through the existing GitHub Pages branch workflow.

## Editing content

- `_data/profile.yml`: public profile, Chinese introduction, links, and experience.
- `_data/research.yml`: three research themes and five project narratives. Keep status labels accurate.
- `_data/publications.yml`: published articles, full author lists, DOI links, and citations. Metadata checked against the Crossref records for each DOI on 14 September 2026. The homepage selects three first-author articles; Grade2Seg remains a research project.
- `_data/funding.yml`: the awarded NSFC Category C project, number 32602720, scheduled for 2027–2029.
- `_data/gallery.yml`: photographs and descriptive captions. Captions are editorial, not inferred dates or locations.

## Images

The images in `assets/images` are WebP derivatives of existing public repository assets. No generated research results are used.

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

The original images and inherited licensing files remain in the repository. The focus explorer and ROI diagram are explicitly labeled conceptual illustrations. Focus positions are not calibrated depth. The CropSR figure is displayed intact; it is not split into an unverified pixel-aligned comparison slider.

## Rendering and accessibility

English is the main language. The About page includes a Chinese profile with its own language attribute and a direct navigation link. Core content is rendered by Jekyll and remains readable without JavaScript. JavaScript progressively adds the mobile menu, focus control, and publication filters. Citation disclosures use native HTML details. Reduced motion, keyboard focus, image dimensions, and legacy URLs are supported.

The old downloadable CV is not presented as current. About is the maintained web CV; do not add a download until an up-to-date public document is available.

## Development

Run `bundle install` and `bundle exec jekyll serve`. The Gemfile pins the GitHub Pages-compatible Jekyll 3.10 series. Run `bundle exec jekyll build` before publishing. Do not commit `_site`, local dependency directories, or dated backup clones.

Existing paths `/research`, `/publications`, `/cv`, `/hobby`, and `/contact` are preserved. The pre-redesign baseline commit is `c220b6cf7357e063525fdeb11d786d365565b9eb`.

Design guidance was consulted from https://github.com/nextlevelbuilder/ui-ux-pro-max-skill. The final direction uses this site's own research and photographic material, warm paper, deep green, copper accents, serif headlines, and restrained interaction.
