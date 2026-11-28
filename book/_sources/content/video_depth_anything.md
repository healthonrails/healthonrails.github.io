# Video Depth Anything (Per-Frame Depth Estimation)

Annolid bundles the [Video-Depth-Anything](https://github.com/DepthAnything/Video-Depth-Anything) model family so you can estimate smooth, temporally consistent per-frame depth maps directly from any loaded video — inside the GUI or from Python scripts.

Use depth sidecars (`depth.ndjson`) when you want:

- monocular **2D-to-3D pose lifting** (for example into [Rat NCAP or FlyBody 3D twins](../tutorials/Simulation_3d_digital_twins.md)),
- **point-cloud exports** (`point_clouds/*.csv`) for 3D scene visualization, or
- **rearing / vertical-height signals** from a single overhead or angled camera.

## Prerequisites

Install the GUI + ML runtime extras (or use the `tracking` / `workstation` installer profile):

```bash
pip install "annolid[gui,ml]"
```

For headless Python scripting without the GUI, `pip install "annolid[ml]"` is sufficient. (For optional `.exr` floating-point depth export, also install `OpenEXR` and `Imath`.)

## Step-by-Step GUI Workflow

1. Open your video in Annolid (`File → Open Video`).
2. *(Optional)* Configure encoder size, target resolution, frame limit, metric-depth mode, and export artifacts via **`View → Depth Settings…`**.
3. Run **`View → Video Depth Anything…`**.
4. Watch streaming progress in the status bar and inspect the live depth overlay right on the video canvas.
5. Annolid writes `depth.ndjson` (plus any optional visualizations or point clouds) into your chosen output directory.

```{tip}
**Streaming mode** is enabled by default: Annolid processes frames incrementally with low RAM overhead so even long recordings stay smooth.
```

## Pre-Downloading Checkpoints (Optional)

Annolid auto-downloads the chosen checkpoint into `annolid/depth/checkpoints` on first run. To prefetch models ahead of time on a shared lab workstation:

```bash
# List available depth checkpoints
python -m annolid.depth.download_weights --list

# Download a specific model (ViT-L relative or ViT-B metric depth)
python -m annolid.depth.download_weights --model video_depth_anything_vitl
python -m annolid.depth.download_weights --model metric_video_depth_anything_vitb
```

## Scripted Python Workflow

```python
from pathlib import Path
from annolid.depth import run_video_depth_anything

result = run_video_depth_anything(
    input_video=str(Path("videos/mice.mp4")),
    output_dir=str(Path("outputs/mice_depth")),
    encoder="vitb",
    max_res=900,
    max_len=500,
    target_fps=15,
    save_depth_video=True,
    save_depth_frames=True,
    save_point_clouds=True,
)
print("Depth NDJSON written to:", result["depth_ndjson"])
```

## Output Files Explained

| Output | Description |
| --- | --- |
| `depth.ndjson` | Primary per-frame sidecar storing quantized `uint16` PNG depth maps + scale metadata under `otherData.depth_map`. |
| `<video_stem>_vis.mp4` | Optional colorized depth preview video (`save_depth_video=True`). |
| `depth_frames/` | Optional individual depth image frames (`save_depth_frames=True`). |
| `point_clouds/*.csv` | Optional 3D point-cloud tables (`save_point_clouds=True`). |
| `<video_stem>_depths.npz` / `_depths_exr/` | Optional raw NumPy array or OpenEXR depth stacks (`save_npz=True` / `save_exr=True`). |

```{note}
For advanced configuration flags and troubleshooting, see the [Video Depth Anything Reference](https://annolid.com/portal/video_depth_anything/) on the Annolid Docs Portal.
```
