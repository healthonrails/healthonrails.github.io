# Extracting Frames (Optional Workflow)

```{note}
**Frame extraction is optional.** For standard tracking with Cutie, SAM3, DINOv3, or INSID3, simply open your video directly via **`File → Open Video`**, jump to a clean seed frame, draw your shapes, and press **`Ctrl+S`**.
```

Use **Extract Frames** when you want an explicit image directory for:

- building a static training dataset across diverse frames (for **YOLO** or **COCO** export),
- sampling evenly spaced or high-motion keyframes (for example with *k*-means or optical-flow sampling) across multiple recordings, or
- sharing a lightweight folder of PNG images with collaborators for labeling or inter-rater review.

## Extract Frames in the GUI

```{figure} ../images/showcase/extract_frames_dialog.png
---
name: extract-frames-gui-dialog
alt: Annolid Extract Frames dialog showing video selection, output folder, number of frames, and sampling algorithm
width: 72%
---
Open the **Extract Frames** dialog from the main toolbar (`Extract frames`) or `File` menu to sample diverse keyframes into an image folder.
```

1. Click **`Extract frames`** on the left side of the main toolbar.
2. Select your source video file and destination folder.
3. Choose how many frames to sample (for an initial custom YOLO training pass, **20–60 diverse frames per video** is a strong starting point).
4. Choose a sampling strategy:
   - **Uniform / Fixed interval**: evenly spaced across the recording.
   - **Motion / Visual diversity**: prioritizes frames where posture or position changes rather than idle resting frames.
5. Click **Run**. Once finished, click **`Open Dir`** in Annolid to step through the extracted frames and annotate them.

## Extract Frames From the Command Line

You can also extract frames headlessly using FFmpeg or Annolid's `sim2real sample` diverse coreset sampler:

```bash
# Extract 1 frame every 2 seconds with FFmpeg
mkdir -p frames_out
ffmpeg -i trial_01.mp4 -vf "fps=0.5" frames_out/trial_01_%06d.png

# Diverse foreground + motion coreset sampling (K-Means medoids + Farthest-Point Sampling)
annolid-run sim2real sample \
  --video trial_01.mp4 \
  --project ./sampled_frames_proj \
  --sampling-strategy diverse \
  --samples-per-video 30
```

```{tip}
Looking for more details on video-first vs. frame-folder workflows? Visit the [Workflows Guide](https://annolid.com/portal/workflows/) on the Annolid Docs Portal.
```

Next: start annotating your first frame in [Labeling Instances, Keypoints & Zones](labelling_images.md).
