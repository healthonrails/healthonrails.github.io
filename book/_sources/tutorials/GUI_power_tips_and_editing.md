# GUI Power Tips: Merging Shapes, Reordering Lists & Class Maps

Small canvas habits save hours during real annotation sessions. This chapter collects Annolid's most helpful desktop editing tricks in one place.

## 1. Merge Split Polygons or Mask Fragments

When SAM or a tracker splits one animal into two adjacent pieces (for example a torso + tail fragment), merge them cleanly into one shape without redrawing:

1. Switch to **Edit Polygons** mode on the standard image/video canvas.
2. In the **Label Instances** list, select two or more matching shapes with **`Ctrl+Click`** (macOS **`Cmd+Click`**).
3. Click **`Edit → Merge Selected Shapes`** (or right-click the selected shapes → **Merge Selected Shapes**).
4. Supported merge types:
   - **Vector shapes** (`polygon`, `rectangle`, `oriented_rectangle`) → unified into one exact combined polygon.
   - **Mask fragments** (`mask`) → unioned into one tight-cropped mask.
5. Press **`Ctrl+Z`** anytime to undo cleanly back to the original fragments.

```{note}
Shapes must be unlocked (`Ctrl+Shift+L`), visible, and share the same label, `group_id`, flags, and metadata before merging. Mixed vector+mask selections or disconnected polygons are rejected safely without modifying your originals.
```

## 2. Drag-to-Reorder Annotation Lists & Paint Depth

You can drag rows up or down directly inside both right-hand label lists:

- **In `Label Instances`**: Reorders the shapes on the canvas and in the saved JSON! **Later rows paint on top of earlier rows**, which is handy when a small keypoint or foreground animal sits over a larger background zone. Supports multi-row drag (`Ctrl/Cmd+Click` or `Shift+Click`) and full `Ctrl+Z` Undo.
- **In `Labels` (summary list)**: Changes only your display order for the current session without modifying saved JSON files or marking the frame dirty.

Reordering never renames labels or alters tracking identities.

## 3. Lock Stable Class IDs With `project.annolid.json`

Nothing breaks a YOLO training run faster than class IDs shifting between videos (`0=mouse, 1=feeder` in video A vs. `0=feeder, 1=mouse` in video B).

1. Open **`File → Project Schema…`** and define your canonical label/behavior list once in `project.annolid.json` at the root of your project folder.
2. Annolid's **Flags** panel, **Timeline**, and **LabelMe → YOLO** converter automatically walk upward from your dataset folder to discover `project.annolid.json` and lock identical numeric class IDs across every export!
3. Run the automated pose/YOLO builder from the CLI:

```bash
# Auto-discovers project.annolid.json class IDs (or override with --labelme2yolo-class-map)
python -m annolid.main \
  --labelme2yolo /path/to/labelme_dataset \
  --val_size 0.1 \
  --test_size 0.1

# Automated pose dataset builder with dataset_summary.json coverage report
python -m annolid.main \
  --build_pose_dataset /path/to/labelme_dataset \
  --pose_output /path/to/output_dataset \
  --val_size 0.1 \
  --test_size 0.1
```

## 4. One-Click Reusable Zone Presets

Drawing a 9-chamber arena by hand every session is tedious. Open **`Video Tools → Zones`** to:

- drop a **3×3 Chamber Layout** or **3×3 Social Door Layout** preset onto the canvas in one click,
- resize, rename, or recolor any chamber,
- save as `<rig>_zones.json` (`semantic_type=zone`), and reuse that single zone file across every future recording from the same behavioral rig!
