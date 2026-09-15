# Research figures: sources and generation

The Research page pairs every project with a figure. Newly restored historical figures are preserved and re-encoded losslessly as WebP; all labels, results, and content remain unchanged. Click any figure to inspect the full image.

## New conceptual illustrations

Two original illustrations were generated with the built-in image_gen tool (not the API/CLI), for explaining ongoing work. They depict conceptual components and annotations, not a real apparatus, customer image, measured response, or validated segmentation result. Multi-focus z1–z3 labels denote focus indices, not calibrated physical depth. A Sunny Optical reference is presented separately as accessible webpage text.

- `assets/images/multi-focus-optics.webp`: lens assembly, optical rays, and focus-dependent defect appearance.
- `assets/images/optical-localization.webp`: concentric lens fits and sensor-region localization.

Industry reference: [Sunny Optical product categories](https://www.sunnyoptical.com/en/products.html) and [Sunny Instruments lens AOI example](https://www.sunny-instrument.com/en/products-detail/81). These support the lens manufacturing/inspection context; no product-specific design, specifications, performance claims, or company branding are copied. The company relationship wording follows the homepage owner's instructions.

### Multi-focus illustration prompt

Use case: scientific-educational.
Asset type: scientific illustration for Xiangyu Lu's academic homepage, research entry "Multi-focus defect perception in optical components". Make a finished wide landscape image, approximately 3:2 aspect ratio, not a website mockup.
Primary request: a refined, scientifically legible illustration of multi-focus LENS defect inspection for optical manufacturing, drawing on the industry context of Sunny Optical / 舜宇. The physical object is a camera lens module with glass lens elements and concentric mounting structure, not biological tissue, a microscope slide, or a decorative crystal.
Composition: one coherent scene on a very pale gray-sage background. On the left, a restrained semi-realistic 3D cutaway of a small charcoal camera lens barrel, with several transparent curved glass elements along one optical axis, restrained cyan coating reflections, and thin optical ray lines indicating the lens-based imaging context. On the right, three evenly sized circular monochrome inspection images stacked diagonally with a little separation, showing the SAME concentric lens rim and the same localized small defect coordinate. Label these three planes exactly "z1", "z2", "z3"; these are focus indices, not calibrated physical depth. In the middle plane the small scratch/particle-like defect is sharp; in the other two it is blurred/fainter. A tiny warm amber contour marks this one localized anomaly and a fine guide connects its spatial location across the three focus images. Keep all normal structure otherwise consistent.
Scientific meaning: joint spatial and focus-dependent appearance, separating a localized abnormal response from normal annular lens structure. This is a conceptual illustration, never a claim of measured data or actual apparatus.
Visual style: polished journal graphical abstract meets restrained industrial design illustration, realistic glass and machined metal, precise lines, gentle natural shading, plenty of calm background; intellectually engaging without looking stiff. Palette slate, silver, desaturated sage, clear cyan glass and one tiny amber accent. No neon, no saturated rainbow, no dark sci-fi backdrop, no infographic boxes, no decorative charts, no neural network spaghetti.
Text: only short labels "Lens assembly" and "Focus sequence" plus "z1", "z2", "z3", in clean dark sans-serif, readable at reduced size. No brand logo, no company wordmark, no device serials, no accuracy percentages or results. Branding/context will be supplied as accessible webpage text. No outer frame, no watermark.

### Localization illustration prompt

Use case: scientific-educational.
Asset type: original scientific illustration for an academic personal website, research entry "Geometry-guided optical localization". A finished wide landscape image approximately 3:2 ratio, not a website mockup.
Subject: localizing the inner and outer rings of a lens and the active area of an image sensor chip, using geometry and image structure to refine a proposed region of interest.
Composition: two physical inspection objects side-by-side on a calm very pale gray-sage background. Left: a nearly top-down, slightly isometric small charcoal machined camera lens barrel with realistic clear glass and subtle cyan coating. Right: a rectangular CMOS image sensor die in a dark ceramic package with delicate gold contacts. Draw crisp, restrained teal geometry annotations aligned correctly to the physical boundaries: two concentric fitted circles and a small center cross on the lens, and a fitted rectangle and precise corner markers on the sensor active area. A faint dashed gray initial bounding box around each object suggests a coarser proposal. Underneath, a simple thin-arrow relation with only these exact words: "Proposal" followed by "Geometry" followed by "Refined ROI". Above or near the two objects the short labels "Lens" and "Sensor". The annotations should be plainly illustrative, not a screenshot from real measurement software.
Style: technically accurate in spirit, polished editorial scientific illustration with subtly realistic 3D material rendering, fine linework and soft shadows. Fits a simple premium academic website. Slate metal, silver, desaturated sage/teal outlines, tiny restrained gold hardware details. Calm generous spacing, coherent viewpoint, clean high legibility at thumbnail scale.
Constraints: conceptual illustration only, no performance curves, no confidence scores, no made-up dimensions, no coordinates, no physical tolerances, no extra text, no brand/logo/watermark. No flashy neon, no glowing sci-fi circuitry, no excessive translucent cards, no checkerboard background. No defects highlighted here: this figure is about geometry and localization, distinct from multi-focus defect perception.

## Original research figures

| Web asset | Original public repository image | Context |
| --- | --- | --- |
| cropsr.webp | assets/img/r12_cropsr.png | EVADM / CropSR, ISPRS JPRS 2024 |
| grade2seg.webp | assets/img/fig6_weakly_supervised.png | Grade2Seg research project |
| paddyseg.webp | assets/img/r10_paddySeg.png | Rice phenology segmentation, Drones 2023 |
| direct-geolocation.webp | assets/img/r9_dgl.png | Direct geo-location from the same Drones 2023 work |
| get-model.webp | assets/img/r8_getModel.png | GeT, JKSU-CIS 2022 |
| algal-mapping.webp | assets/img/r11_algalDet.png | Algal-bloom mapping project, 2023 |
| citrus-sizing.webp | assets/img/r7_sizer.png | Citrus sizing project, 2020 |
| libs-spectroscopy.webp | assets/img/r5_pca.png | LIBS undergraduate thesis, 2020 |

Historical project descriptions come from the original public homepage backed up at commit c220b6cf7357e063525fdeb11d786d365565b9eb. Published work uses the corrected publication years already verified in the site's publication data. PaddySeg and direct geo-location remain one research entry, because they belong to the same publication. Original paper figures are not replaced by generated depictions of experimental results.
