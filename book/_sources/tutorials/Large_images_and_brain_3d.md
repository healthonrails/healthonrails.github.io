# Large TIFF, Atlas Overlays & Brain 3D Reconstruction

Beyond behavioral videos, Annolid supports **gigapixel / multi-page microscopy TIFFs (`.tif`, `.tiff`, `.ome.tif`)**, **Illustrator vector atlas overlays (`.svg`, `.ai`, `.pdf`)**, and interactive **sagittal-to-coronal Brain 3D reconstruction** — keeping every edited polygon compatible with standard LabelMe page annotations.

```{figure} ../images/diagrams/brain_3d_reslicing_workflow.png
---
name: brain-3d-workflow-diagram
alt: Four-stage pipeline from Large TIFF Stack and Atlas Overlay through Build Brain 3D Model to Coronal Reslicing and synchronized 3D preview
width: 100%
---
Annolid connects tiled large-image microscopy, landmark-aligned vector atlases, and editable sagittal-to-coronal 3D brain region reconstruction in one workflow.
```

## 1. Install Optional Large-Image Support

Standard `annolid[gui]` installs launch normally without large-image dependencies. For gigapixel whole-slide or multi-page OME-TIFF microscopy, install the optional `large_image` extra:

```bash
pip install "annolid[large_image]"
```

This activates `tifffile`, `pyvips`, and `openslide-python` when available (installing native `libvips` or OpenSlide gives the fastest tiled pan/zoom responsiveness).

## 2. Fast Viewing & Vector Atlas Alignment

1. Open your `.tif` / `.ome.tif` via **`File → Open`**.
2. For very large non-pyramidal TIFFs, run **`File → Optimize Large TIFF for Fast Viewing…`** to build a reusable pyramidal cache (manage disk space anytime under **`File → Large TIFF Cache Info…`** or **`Clear Current TIFF Cache…`**).
3. Import an anatomy drawing via **`File → Import Vector Overlay…`** (`SVG`, PDF-compatible Illustrator `.ai`, or `.pdf`). Annolid preserves the imported source geometry as immutable provenance and creates an editable correction layer on top.
4. Use the unified **Layers** and **Vector Overlays** docks to adjust visibility, opacity, scale, rotation, and z-order.
5. **Landmark-based affine alignment**: Place corresponding landmarks on your histology image and vector overlay, click **`Pair Selected`** for 3+ matches, and click **`Align Points`**.
6. Export corrected contours via **`File → Export Corrected Overlay…`** (`SVG`, overlay JSON, or LabelMe JSON).

## 3. Sagittal-to-Coronal Brain 3D Reconstruction

When you have annotated polygons across a stack of sagittal brain sections and want synchronized coronal contours plus a 3D mesh preview:

1. Open your sagittal stack and annotations in Annolid.
2. Run **`View → Build Brain 3D Model…`** and configure coronal spacing or plane count, contour point resampling, longitudinal/in-plane smoothing, and optional reference snapping.
3. Open the dock via **`View → Open Brain 3D Session`** and generate coronal slices with **`View → Regenerate Coronal Planes`**.
4. Open the interactive Three.js 3D preview via **`View → Open Brain 3D Preview`** — clicking any region in 3D automatically highlights the region in the dock and jumps to the nearest coronal plane!

### Iterative Coronal Editing Loop
1. Select a coronal plane in the **Brain 3D Session** dock and refine any polygon directly on the 2D canvas.
2. Use **`Create Region On Plane`**, **`Hide Region On Plane`**, or **`Restore Region On Plane`** to control regional presence cleanly.
3. Click **`Apply Current Edits`** (or press `Ctrl+S`): Annolid updates the canonical 3D artifact (`otherData["brain_3d_model"]`) first and regenerates affected nearby coronal planes automatically.

```{note}
If you later modify the original sagittal source polygons, Annolid flags the canonical 3D artifact as invalidated so you can rebuild cleanly rather than silently serving stale coronal slices. See [Large TIFF & Atlas Overlays](https://annolid.com/portal/atlas_overlay_workflow/) and [Brain 3D Reconstruction](https://annolid.com/portal/brain_3d_reconstruction/) on the Docs Portal for detailed API references.
```
