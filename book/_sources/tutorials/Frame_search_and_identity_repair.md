# Semantic Frame Search & Automated Identity Repair

Working with multi-hour recordings? Two power tools in Annolid save hours of manual scrubbing:

1. **Semantic Frame & Behavior Search (`ONNX EmbeddingGemma 2`)** — find rare behavioral moments by typing plain English (`mouse grooming`, `nose-to-nose sniffing`, `rearing on hind legs`) with **no PyTorch required**.
2. **Identity Governor** — audit and automatically repair stubborn multi-animal identity swaps across thousands of frames using explicit, reproducible zone/distance/area evidence rules.

---

## Part 1: Find Rare Behaviors in Seconds (ONNX EmbeddingGemma 2)

Annolid integrates **ONNX EmbeddingGemma 2** (`onnx-community/embeddinggemma-2-ONNX`, Apache 2.0, ungated), mapping text, individual video frames, and multi-frame temporal clips (`4f` / `8f`) into one shared 768-dimensional semantic space — running cleanly on **ONNX Runtime** (~270 MB `q4` download, no PyTorch needed).

### Search Inside the GUI (`Embedding Search` Dock)
1. Open your video in Annolid (`File → Open Video`).
2. Open **`View / Tools → Frame Search (Embedding)`**.
3. Keep the default **EmbeddingGemma 2 (ONNX)** backend and pick a speed/detail preset:
   - `Q4 · 140t · 768d` *(default balanced)*
   - `Q4 · 70t · 256d (fast)` *(2–5× faster on CPU)*
   - Temporal window: `1f (frame)`, `4f (clip)`, or `8f (clip)` for dynamic actions like chasing or rearing.
4. Keep **Auto** thresholding enabled (adaptive MAD-based threshold calibrated to EmbeddingGemma 2's cosine cone).
5. Type a natural-language query (`mouse grooming`, `mounting`) and press **Enter** — or navigate to an example frame and click **Search** to find visually similar moments!
6. **Double-click any match** to jump straight to that frame, or select matching rows and click **`Label Selected`** to write intervals directly into your behavior log.

```{tip}
Once a video is indexed into Annolid's disk `.npz` cache, follow-up searches for *different* behaviors return results in **milliseconds**!
```

### Fast CLI Behavior Search (`annolid-run behavior-search`)

```bash
# Index once and search by natural-language query
annolid-run behavior-search /path/to/video.mp4 \
  --query "mouse grooming" \
  --quantization q4 \
  --soft-tokens 140 \
  --matryoshka-dim 256 \
  --stride 5 \
  --index-cache ./video_eg2_index.npz \
  --out ./grooming_matches.json \
  --json

# Reuse the cached index for a second behavior in milliseconds
annolid-run behavior-search /path/to/video.mp4 \
  --query "rearing on hind legs" \
  --index-cache ./video_eg2_index.npz \
  --json

# Zero-shot multi-behavior scoring across the timeline
annolid-run behavior-search /path/to/video.mp4 \
  --behaviors "grooming,rearing,sniffing,resting" \
  --clip-frames 4 \
  --stride 10 \
  --out ./behavior_scores.json \
  --json
```

---

## Part 2: Automated Identity Repair (Identity Governor)

For isolated identity swaps during Cutie/SAM3 tracking, fixing 1 anchor frame and re-propagating is still the fastest path. When you have **large batches of already-tracked frame JSONs** and clear assay evidence (for example a tethered resident vs. untethered intruder, chamber-restricted animals, or consistent size differences), **Identity Governor** audits and repairs swaps reproducibly with a dry-run report.

```{figure} ../images/showcase/mouse083_behavior_storyboard.png
---
name: search-identity-storyboard
alt: Four-panel storyboard showing normal tracking, close contact, and an occlusion event caught by Track QC
width: 96%
---
Close dyadic contact and occlusions (Panels C–D) are the primary moments where multi-animal trackers risk swapping IDs — pair Track QC with Identity Governor to audit and repair them cleanly.
```

### Run Identity Governor in the GUI
1. Open **`Video Tools → Identity Governor…`** (or **`Analysis → Identity Governor…`**).
2. Load a built-in policy snippet (*Generic identity template*, *2-subject arena (zone + distance)*, *3-vole social assay*, or *Distance-only fallback*).
3. Always run **Dry Run** first to inspect the generated audit report before applying atomic JSON rewrites!

### Scripted Python API (Dry-Run → Apply)

```python
from annolid.postprocessing import run_identity_governor

policy = {
    "metric_aliases": {
        "in_left": "zone.inside.left_zone",
        "in_right": "zone.inside.right_zone",
        "nearest": "distance.nearest",
        "area_px": "area",
    },
    "rules": [
        {
            "name": "resident_when_right_and_large",
            "assign_label": "resident",
            "conditions": [
                {"metric": "in_right", "op": "eq", "value": True},
                {"metric": "area_px", "op": "gte", "value": 80.0},
            ],
            "min_streak_frames": 2,
            "priority": 10,
        },
    ],
    "ambiguity_conditions": [{"metric": "nearest", "op": "lte", "value": 5.0}],
    "max_backtrack_frames": 500,
    "canonical_track_ids": {"resident": "1", "intruder": "2"},
}

# Dry-run first (apply=False writes only the audit report)
report = run_identity_governor(
    annotation_dir="/path/to/video_annotations",
    zone_file="/path/to/session_zones.json",
    policy=policy,
    apply=False,
)
print("Proposed frame repairs:", report.get("total_repairs"))
```

```{tip}
Want to embed audio vocalizations (`.wav`) alongside video frames in EmbeddingGemma 2, or configure advanced backtracking spans in Identity Governor? See the [Behavior Embedding Search](https://annolid.com/portal/behavior_embedding_search/) and [Identity Governor](https://annolid.com/portal/identity_governor/) guides on the Docs Portal.
```
