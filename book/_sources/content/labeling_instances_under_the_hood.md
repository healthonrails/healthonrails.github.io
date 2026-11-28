# AI-Assisted Labeling: Point & Text Prompts

Annolid accelerates manual annotation by letting you prompt foundation models with either **clicks** (point prompts) or **plain words** (text prompts) — and converts every predicted mask straight into an editable polygon on your canvas.

## 1. Point Prompts (`Create AI-Polygon`)

When you select **Create AI-Polygon** from the canvas right-click menu:

1. Choose an interactive segmentation backend from the **AI Model** selector (for example **EfficientSAM** for fast CPU/laptop response, or **SAM2 / SAM3** for fine edges and complex bedding).
2. Click inside the target animal or object — Annolid computes a binary mask and simplifies its boundary into a crisp, editable polygon.
3. Click additional points if needed to refine thin regions (like ears or tails), then **Ctrl+Left-Click** (`Cmd+Left-Click` on macOS) to confirm and assign a label.

```{figure} ../images/AI_polygon.png
---
name: under-hood-ai-polygon
alt: Right-clicking the Annolid video canvas to select Create AI-Polygon
width: 92%
---
Selecting **Create AI-Polygon** from the canvas context menu with EfficientSAM active.
```

### Video walkthrough: Point-prompt labeling

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/YOnUnpwkLFc" title="AI-Polygon point-prompt labeling in Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 2. Text Prompts (Grounding DINO → SAM & SAM3)

When you have multiple animals or arena objects on screen and want to bootstrap masks without clicking each one:

1. Enter comma-separated phrases in the **Text Prompt** field in the top toolbar — for example:
   - `mouse`
   - `black mouse, white mouse`
   - `mouse, feeder, water bottle`
2. You can also use **label aliases** with SAM3 text mode so the visual query maps straight to your study's canonical label name:
   - `black mouse=resident, white mouse=intruder`
   - `black mouse -> resident; white mouse -> intruder`
3. Annolid runs **Grounding DINO → SAM** (or **SAM3** windowed propagation) to detect boxes, refine segmentation masks, and place editable polygons onto the frame.

### Video walkthrough: Text-prompt labeling

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/bCCobNAwWvM" title="Text-prompt segmentation with Grounding DINO and SAM in Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Practical Tips for Clean AI Polygons

- **Start on an unoccluded frame**: Give the segmentation model a clear view of each animal's silhouette before launching video tracking.
- **Tweak vertices only where it matters**: Minor boundary fuzz on a tail tip rarely hurts tracking, whereas merged masks between two touching animals should be separated before pressing **Pred**.
- **Switch models anytime**: Because every AI backend writes the exact same LabelMe polygon format, you can seed frame 0 with **EfficientSAM**, track with **Cutie** or **SAM3**, and later add keypoints with **DINOv3**.

Next: see the full end-to-end [mouse083 Resident-Intruder Walkthrough](../tutorials/mouse083_resident_intruder_showcase.md) or follow the step-by-step [Tracking with Cutie](tracking_with_Cutie.md) guide.
