# Troubleshooting & Frequently Asked Questions

Stuck on an error message, slow tracking, or model download? Click any question below for a quick, verified fix.

## Installation & Startup

::::{dropdown} `qtpy.QtBindingsNotFoundError` when launching `annolid`
You installed the base package without the desktop Qt bindings. Install the `gui` extra into your active environment:

```bash
pip install "annolid[gui]"
```

Confirm with `annolid --version` and `annolid --help`.
::::

::::{dropdown} Do I need Detectron2 or PyTorch just to annotate videos?
**No!** `pip install "annolid[gui]"` installs a fast, lean desktop shell (`PySide6-Essentials`) with no heavy ML downloads. Optional ML/tracking runtimes (`tracking`, `cutie`, `sam3`, `yolo`) install on demand when first used, or upfront via `annolid-run runtime install tracking sam3`. Detectron2 is only needed for legacy Mask R-CNN notebooks (which run easiest on [Google Colab](Annolid_on_Google_Colab.md)).
::::

::::{dropdown} How do I install Annolid on an air-gapped / offline lab PC?
Export a checksummed wheelhouse on an online machine with the matching OS and Python version, copy it over USB, and install offline:

```bash
# Online machine
annolid-run runtime bundle --profile workstation --out ./annolid-wheelhouse

# Offline machine
annolid-run runtime verify-bundle ./annolid-wheelhouse
annolid-run runtime install --profile workstation --wheelhouse ./annolid-wheelhouse --offline
```
::::

## Videos, Codecs & Performance

::::{dropdown} My video won't open, freezes while scrubbing, or tracks very slowly
1. Ensure **FFmpeg** is installed (`ffmpeg -version`).
2. Re-encode uncompressed `.avi` or 4K footage to H.264 `.mp4` at ~640–960 px wide using **`File → Downsample Videos`** (scale `0.5`) or:
   ```bash
   ffmpeg -i raw.avi -vf "scale=960:-2" -c:v libx264 -crf 18 -preset fast ready.mp4
   ```
Downsampling 4K/1080p videos speeds up Cutie, SAM3, and DINOv3 by **4×–10×** with negligible accuracy loss in standard arenas.
::::

::::{dropdown} Large TIFF histology images pan slowly
Install `pip install "annolid[large_image]"` (with native `libvips` or OpenSlide when available), then run **`File → Optimize Large TIFF for Fast Viewing…`** to build a reusable pyramidal cache. Manage cache space under **`File → Large TIFF Cache Info…`**.
::::

## AI Models, Checkpoints & Hugging Face Auth

::::{dropdown} DINOv3 or INSID3 fails with HTTP 401 / 403 / gated repo error
Meta's DINOv3 checkpoints on Hugging Face require one-time license acceptance:
1. Visit the model page (for example `facebook/dinov3-vits16-pretrain-lvd1689m`) and accept the terms.
2. Authenticate once in your terminal: `hf auth login` (or set `HF_TOKEN`).
3. Prefer an open ungated fallback right away? Select `facebook/dinov2-base` in **Tools → Advanced Parameters → Tracker → DINO feature model**.
4. Prefetch or verify local cache with `annolid-run dinov3-models --local-files-only --model <model-id>`.
::::

::::{dropdown} Where does Annolid store downloaded checkpoints?
- TAPNext ONNX and distilled Cutie checkpoints: `~/.annolid/workspace/downloads/`
- Hugging Face models (DINOv3, CoWTracker, EmbeddingGemma 2): standard HF cache (or `DINOV3_LOCATION=/path/to/shared_cache`)
- Video Depth Anything checkpoints: `annolid/depth/checkpoints/`
::::

## Tracking Accuracy, Occlusions & Identity Swaps

::::{dropdown} Two animals swapped IDs after crossing — do I need to re-track the whole video?
**No!**
1. Run **[Track QC](../tutorials/Reporting_and_track_qc.md)** (`annolid-run track-qc` or `/qc` in Annolid Bot) to jump straight to the first error frame.
2. Fix that **one** frame and save (`Ctrl+S`), then clear stale future predictions and click **`Pred`** — Cutie resumes forward from your new manual anchor!
3. For already-tracked pose folders, use **`annolid-run swap-pose --start-frame <N> --instance-a mouse_1 --instance-b mouse_2`** (or **[Identity Governor](../tutorials/Frame_search_and_identity_repair.md)** for automated rule-based repair).
::::

::::{dropdown} How do I retrack a video without losing my manual seed frames?
Delete only the auto-generated `*_tracking.csv`, `*_tracked.csv`, `*_gaps_report.*`, and `<video>_annotations.ndjson` files while keeping your manually labeled `<video>_#########.png` and `.json` pairs inside `<video>/`. See [Segment-Based Batch Tracking](../tutorials/Segment_based_batch_tracking.md).
::::

Still stuck? Open a ticket with your OS, `annolid --version`, and a minimal traceback via [Community & Support](get_in_touch.md).
