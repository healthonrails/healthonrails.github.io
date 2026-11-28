# Point Tracking with TAPNext (ONNX) & CoWTracker

When you want to track specific anatomical landmarks, limb joints, or a grid of surface points — without drawing full segmentation masks or training a supervised pose network — Annolid gives you three complementary training-free point trackers under one unified output contract: **[DINOv3 Keypoints](DINOv3_keypoint_tracking.md)**, **TAPNext (ONNX)**, and **CoWTracker**.

```{figure} ../images/diagrams/point_trackers_comparison.png
---
name: pt-trackers-comparison
alt: Four-column comparison of DINOv3 Keypoints, TAPNext ONNX, CoWTracker, and YOLO-Pose/KPSEG
width: 100%
---
Every point-tracking backend in Annolid reads the same manual seed points (or polygon regions) and writes reviewable LabelMe JSON files.
```

## 1. TAPNext (ONNX) — Fast, PyTorch-Free Point Tracking

**TAPNext (ONNX)** runs purely on **ONNX Runtime** (no PyTorch required), making it ideal for laptops, lightweight workstations, or fast point-grid tracking inside a polygon.

### What TAPNext Accepts as Prompts
- **`point` shapes**: each labeled point (`head`, `tail_base`, `left_wing`) becomes an individually tracked landmark.
- **`polygon` shapes**: Annolid automatically samples a grid of tracked points inside the polygon.
- **Zone shapes**: ignored automatically so arena boundaries stay fixed.

### Installation & Verified Model Cache

```bash
pip install "annolid[gui,tracking]"
```

On first use, Annolid downloads the official TAPNext ONNX model (~938 MB), verifies its SHA256 checksum (`4fca0951...4ba5c5300`), and caches it at `~/.annolid/workspace/downloads/tapnext.onnx`.

### GUI Steps
1. Open your video in Annolid (`File → Open Video`) and scrub to a clean starting frame.
2. Add manual **`point`** labels for your target landmarks (or a `polygon` if you want a sampled grid of points) and press **`Ctrl+S`**.
3. Select **TAPNext (ONNX)** from the **AI Model** dropdown and click **`Pred`**.
4. Review a short segment first to confirm clean tracking before running the full video.

---

## 2. CoWTracker — Windowed Point Tracking

**CoWTracker** uses a windowed temporal tracker (backed by Annolid's bundled VGGT subset) under the exact same prompt and output contract as TAPNext and CoTracker.

### Installation

```bash
pip install "annolid[gui,tracking,cowtracker]"
```

*(If you already have the tracking runtime installed, adding `pip install "safetensors>=0.4.0"` is sufficient.)*

### GUI Steps
1. Open your video and save at least one manual **`point`** or **`polygon`** seed frame (`Ctrl+S`).
2. Choose **CoWTracker** from the **AI Model** dropdown and click **`Pred`**.
3. Validate a short representative clip first — first-run startup includes fetching the Hugging Face checkpoint and initializing the first tracking window.

## Choosing Strong Seed Points

- Place points on **high-contrast anatomical landmarks** (snout tip, ear bases, tail base, wing hinges, paw joints).
- Avoid uniform flat fur patches, shadows, or motion-blurred frames on Frame 0.
- Use **multiple named points** per animal so body rotation stays unambiguous.
- If a point drifts after an occlusion, fix the first drifted frame, press `Ctrl+S`, and restart from that anchor!

```{tip}
Need a reusable pose model across dozens of unseen videos, or want DeepLabCut/SLEAP evaluation metrics and bone-length filtering? Continue to [Pose Estimation & DeepLabCut / SLEAP Interoperability](Pose_estimation_and_interop.md). For deep backend notes, see the [TAPNext](https://annolid.com/portal/tapnext/) and [CoWTracker](https://annolid.com/portal/cowtracker/) docs on the Portal.
```
