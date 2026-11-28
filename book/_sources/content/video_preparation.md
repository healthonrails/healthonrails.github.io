# Preparing & Compressing Videos

Before tracking a long lab recording, a 30-second video-preparation step can cut tracking time by **4× to 10×** while keeping every animal contour sharp.

```{tip}
**Do you need to extract frames first?** No! Annolid opens `.mp4`, `.avi`, `.mov`, and `.mkv` files directly (`File → Open Video`). Downsample or crop when your raw recordings are very high resolution (1080p / 4K), huge uncompressed `.avi` files, or contain large empty borders around the arena.
```

## When Should You Downsample or Crop?

| Situation | Recommended Action | Why It Helps |
| --- | --- | --- |
| Raw 1080p / 4K recordings (`> 1280 px` wide) | Scale to `0.5` (`~640–960 px` wide) | Dramatically faster Cutie, SAM3, and DINOv3 inference with crisp masks |
| Wide camera showing lab table around the cage | Crop to the arena bounding box | Removes background distractors and shrinks file sizes |
| Uncompressed `.avi` (multiple GB per trial) | Re-encode to H.264 `.mp4` (`libx264`, `-crf 18`) | 10× smaller files and smoother GUI timeline scrubbing |
| Folder of 12+ trials with 1–2 outlier cameras | Use **GUI Downsample Videos** with per-video overrides | Keeps folder defaults clean while recording an auditable `.md` report per video |

## Option 1 (Recommended): Batch Downsample in the Annolid GUI

The built-in **Downsample Videos** dialog handles single files or entire folders and writes a reproducible `.md` audit log + `metadata.csv` next to every processed file:

```{figure} ../images/downsample_gui_processing.png
---
name: prep-downsample-gui
alt: Annolid Downsample Videos dialog showing Scale Factor, FPS, Codec, Denoise, Auto Contrast, and Crop Region controls
width: 90%
---
The **Downsample Videos** dialog (`File → Downsample Videos`) lets you set shared defaults for a folder and review outlier videos one by one.
```

1. Open **`File → Downsample Videos`**.
2. In **`Input / Output`**, select your source video or folder. Leave the output folder blank to automatically write into a safe sibling `<folder>_downsampled/` directory (your original videos are never overwritten).
3. In **`Processing`**, configure folder-wide defaults:
   - **Scale Factor**: e.g. `0.5` halves width and height.
   - **FPS**: leave blank to keep the original frame rate, or check **Use specified FPS** to normalize mixed cameras.
   - **Crop Region**: click **Preview & Crop First Frame** to draw the arena visually.
4. If one or two recordings have a shifted camera angle, click **`Review Videos One by One (Folder Input)`** and click **`Save & Next`** only for the exceptions.
5. Open the **`Run`** tab, check **`Rescale Video`**, and click **`Run Processing`**.

For a complete visual guide to per-video crops and batch overrides, see [Downsample and crop videos](downsample_and_crop_videos.md) and [Batch downsampling with sequential video review](../tutorials/Downsample_video_batch_overrides.md).

## Option 2: Quick FFmpeg CLI Recipes

### Install & Verify FFmpeg

```bash
# macOS (Homebrew)
brew install ffmpeg

# Conda (all platforms)
conda install -c conda-forge ffmpeg

# Verify
ffmpeg -version
```

### Everyday Compression & Rescaling Commands

```bash
# Quick convert AVI -> compact H.264 MP4 at 720x480
ffmpeg -i mouse.avi -c:v libx264 -vf scale=720:480 mouse.mp4

# Visually lossless compression (keep resolution, smaller file)
ffmpeg -i input.mp4 -c:v libx264 -crf 18 -preset fast output.mp4

# Resize to 960px wide while preserving aspect ratio (height auto-rounded to even)
ffmpeg -i input.mp4 -vf "scale=960:-2" -c:v libx264 -crf 20 output.mp4

# Crop to arena region (width:height:x:y) and compress
ffmpeg -i input.mp4 -vf "crop=800:500:120:40" -c:v libx264 -crf 18 cropped.mp4

# Trim a short 30-second test clip starting at 00:01:00 (great for verifying your pipeline)
ffmpeg -ss 00:01:00 -t 30 -i input.mp4 -c:v libx264 -crf 18 test_clip.mp4
```

```{note}
Using `scale=960:-2` instead of `scale=960:-1` ensures the computed height is always divisible by 2 — which H.264 (`libx264`) requires!
```

Next: walk through the full [Downsample and crop videos](downsample_and_crop_videos.md) GUI tool, or jump straight to [Labeling Instances](labelling_images.md).
