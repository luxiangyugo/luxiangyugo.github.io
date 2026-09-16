# Research figures: sources and generation

The Research page pairs every project with a figure. Newly restored historical figures are preserved and re-encoded losslessly as WebP; all labels, results, and content remain unchanged. Click any figure to inspect the full image.

Grade2Seg and PaddySeg were re-encoded from their original full-resolution PNGs with alpha preserved, correcting an earlier conversion that rendered transparent regions black and obscured figure text.

## Current concept illustrations

The page shows `multi-focus-trajectories.png` and `florence2-model-grounding.png`, generated conceptual illustrations in the requested lens-cutaway style. The first emphasizes 25 focus layers and illustrative defect/normal trajectories, with Polar–Fourier reduced to the supporting spatial prior. The second shows image and text entering a visible Florence-2 architecture before grounded regions and subsequent ROI refinement. Captions identify concept imagery and illustrative trajectories. Clicking them opens the same image at full size; “Prototype outputs” opens real archived outputs. See [current prompts and provenance](trajectory-model-figures-20260916.md). The preceding lens-to-Polar and semantic-label illustrations are preserved with [their earlier prompts](optical-concept-figures-20260916.md).

## Archived source-based overviews and linked prototype plates

The earlier compact overviews below are preserved but no longer used as page thumbnails. Their detailed source plates remain publicly linked. All panels in these SVGs use real archived inspection and prototype outputs with vector labels. No image-generation model fabricated, retouched, or augmented this experimental content.

- `assets/images/polar-fourier-overview.svg` shows only three matched image-space crops: input, reconstructed background, and local response. The local response is the recorded alpha-weighted signed perturbation. Polar-domain evidence and the cross-focus research-stage note remain in the linked detailed plate.
- `assets/images/semantic-geometric-overview.svg` shows two short paths: lens proposal to geometric center/circle, and sensor outer region to cropped inner ROI to mapped ROI. Short, verbatim fragments of the recorded prompts use the same colors as the corresponding regions. The sensor context crop enlarges the region for page-size viewing; coordinate mapping is preserved. The lens proposal remains explicitly schematic.

Detailed plates:

- `assets/images/polar-fourier-research.svg` and its `-mobile.svg` variant combine archived MFL104 Polar input, robust harmonic reconstruction, robust residual score, and paired image-space detail. Image panels are cropped from `MFL104_03_polar_diagnostic.png` and `MFL104_02_roi_detail.png`, recovered from the owner's previous research attachments. Colors and intensity values are preserved. Marker A denotes the same polar-domain scratch region across the three corresponding panels. The signed defect layer is the recorded alpha-weighted perturbation layer, not an unweighted physical-defect reconstruction or a final segmentation claim.
- `assets/images/semantic-geometric-localization.svg` and its `-mobile.svg` variant use inspection images and prompt excerpts from the owner's May 2026 Florence-2 research notes. Lens final center/circle and sensor outer/inner rectangles are traced from recorded outputs. The coarse lens candidate outline and grounding arrows are explicitly schematic. The chip AOI is cropped from the same original image used in the full-image views; the coordinate transform is preserved when redrawing the inner ROI. No image is passed off as newly inferred output.

Current source material supports the single-layer mechanism and localization examples. Matched focus strips and measured trajectories are still missing on this host. The detailed plate labels this gap and does not invent curves or imply that persistence alone determines a defect. See [the precise material checklist](research-figure-materials-needed.md).

To reproduce the two overviews and four detailed SVGs, run `python scripts/build-research-panels.py --source-dir <source-folder>` with Pillow installed. The source folder must contain `polar-diagnostic.png`, `roi-detail.png`, `lens-input.png`, and `chip-input.jpeg`; these are the unmodified archived source images described above. The script records exact crop coordinates in `panel-crops.json` and composes presentation overlays without running new inference.

## Archived conceptual illustrations (superseded)

Two original illustrations were generated with the built-in image_gen tool (not the API/CLI), for explaining ongoing work. They depict conceptual components and annotations, not a real apparatus, customer image, measured response, or validated segmentation result. Multi-focus z1–z3 labels denote focus indices, not calibrated physical depth. A Sunny Optical reference is presented separately as accessible webpage text.

- `assets/images/multi-focus-optics.webp`: lens assembly, optical rays, and focus-dependent defect appearance.
- `assets/images/optical-localization-florence2.webp`: Florence-2 semantic proposals, geometry verification, and refined lens/sensor ROIs. The initial geometry-only illustration remains archived as `optical-localization.webp`.

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

Historical project descriptions come from the original public homepage backed up at commit c220b6cf7357e063525fdeb11d786d365565b9eb. All 13 original entries and their buttons are restored in the original order. Published work uses the corrected publication years already verified in the site's publication data. PaddySeg and direct geo-location are separately listed to retain the original structure, with a shared-publication note. Original paper figures are not replaced by generated depictions of experimental results.

Additional restored assets:

| Web asset | Original public asset | Context |
| --- | --- | --- |
| weighing-system.webp | assets/img/r6_weighingSystem.png | 24-channel weighing system |
| seeding-device.webp | assets/img/r3_structure.jpg | Integrated seeding and fertilizing |
| reciprocating-mechanism.png | assets/img/r4_rotation.mp4 | Unaltered still frame at 4 seconds, used as the original video's poster |
| uav-weeds.webp | assets/img/r1_weedsUAV.jpg | Early UAV weed recognition |
| charging-network.webp | assets/img/r2_hm.png | Charging-station network planning |

## Archived Florence-2 conceptual revision (superseded)

The previous conceptual localization figure was edited with the built-in image_gen tool, using the initial illustration as the reference. Final generated source: `C:/Users/luxy/.codex/generated_images/01a0a04e-e534-7a62-bd12-34aebc5224fa/exec-532f27b0-35be-4dcd-8f0b-15589285a659.png`. A copy is preserved at `../20260914/preview/optical-localization-florence2-original.png` relative to the main repository. The superseded asset remains at `assets/images/optical-localization-florence2.webp` (1536 × 1024, WebP quality 92); the active page now uses the source-based SVG panels described above.

### Semantic-guidance edit prompt

Edit the supplied scientific illustration for the research entry "Geometry-guided optical localization with Florence-2". Keep the lens and sensor renderings, precise teal circles/rectangle, faint dashed proposal boxes, pale gray-sage backdrop, muted palette, composition and overall material style.
Make Florence-2 semantic guidance explicit in the explanatory flow. Replace the bottom row with three readable, restrained steps connected by thin arrows:
"Florence-2" with the smaller line "Semantic proposals"
then "Geometry" with the smaller line "Boundary verification"
then "Refined ROI".
The three steps must remain inside the image with generous margins, no overflow and no overlap. Use clean dark sans-serif typography for all labels, including "Lens" and "Sensor" above the physical objects. Add a small restrained text label "lens" attached to the left dashed candidate box and "sensor" attached to the right dashed box, to visually show semantic object identities; keep them readable and inconspicuous. Preserve all physical objects and geometry overlays. Do not imply Florence-2 directly performs the final circle fit; the flow must clearly distinguish semantic proposal generation from geometric refinement. No invented numerical results, brand logos, elaborate neural network drawing, badges, extra decoration, or additional text. Keep landscape 3:2 ratio. This remains a conceptual illustration, not a measurement screenshot.

### Typography correction prompt

Make one typographic correction only to the supplied illustration. The bottom-right label currently has a duplicated final letter and must read exactly "Refined ROI" — spell the acronym R, O, I, with exactly one final I. Use the same clean sans-serif style. Preserve everything else without any change: physical lens, sensor, annotations, all other text ("Florence-2", "Semantic proposals", "Geometry", "Boundary verification", "Lens", "Sensor", small "lens" and "sensor"), arrows, layout, colors, lighting, image size. Do not add any extra characters or labels.
