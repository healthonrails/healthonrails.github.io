# Real-Time Wireless & Multi-Camera Live Detection

Need live detection during an experiment — or automated MP4 clip recording whenever a mouse, rat, or target object enters view? Annolid supports real-time **YOLO11 / YOLO26 / YOLOE** inference over **USB webcams**, **RTSP IP cameras**, **RTP multicast streams**, **MJPEG wireless cameras**, and **multi-camera synchronized ZeroMQ pipelines**.

## Prerequisites

Install Annolid with the `yolo` and `realtime` extras (or the `workstation` / `full` profile):

```bash
pip install "annolid[gui,yolo,realtime]"
```

## 1. Single-Camera & Wireless IP Camera Setup (GUI)

Open the Realtime window in Annolid — the left control panel is split into two clean tabs:

### `Setup` Tab
1. **Select a model**: Pick a built-in YOLO preset (for example `yolo11n-seg.pt` for high FPS) or select **Custom…** to load your own fine-tuned `.pt`, `.onnx`, `.engine`, or `.mlpackage` weights.
   - Enable **View only (no detection or inference)** if you just want to check camera framing without loading a model.
2. **Enter your Camera / Stream source**:
   - USB camera index: `0` (or `1`, `2`)
   - RTSP IP stream: `rtsp://camera-host:554/stream1`
   - RTP multicast: `rtp://@239.0.0.1:5004`
   - Wireless MJPEG URL: `http://camera-host/img/video.mjpeg` *(Annolid also auto-normalizes common camera control pages like `.../img/main.cgi?...`)*
   - Local video file path (for dry-run testing)
3. **RTSP Transport**: Leave on `Auto` (or switch to `TCP` if Wi-Fi packet loss causes gray/broken frames).

### `Run & Output` Tab
1. Tune **Frame Width / Height**, **Max FPS** (for example `15` FPS on wireless cameras), and **Confidence** threshold (`0.25` is a strong default).
2. Enable **Save MP4 segments on detections** to record only meaningful behavioral events:
   - **Segment Targets**: comma-separated classes to trigger recording (e.g., `mouse` or `animal`).
   - **Prebuffer / Postbuffer**: e.g., `2.0 s` before first detection and `3.0 s` after last detection so event onset is never clipped!
   - **Min / Max Duration**: prevents tiny 1-frame noise clips or runaway recordings.
3. Click **`Start Realtime`** to begin and **`Stop`** to finish cleanly.

## 2. Multi-Camera Live Detection (CLI + ZeroMQ)

For multi-view behavioral rigs, launch one perception worker per camera with its own `camera_id`, ZeroMQ publisher port, and output folder:

```bash
# Camera 0 (USB overhead camera)
python -m annolid.realtime.perception \
  --camera-index 0 \
  --publisher tcp://*:5555 \
  --model yolo11n-seg.pt \
  --targets mouse \
  --save-detection-segments \
  --detection-segment-output-dir runs/realtime/overhead_cam

# Camera 1 (Wireless RTSP side camera)
python -m annolid.realtime.perception \
  --camera-index 'rtsp://user:pass@192.168.1.50:554/stream1' \
  --publisher tcp://*:5556 \
  --model yolo11n-seg.pt \
  --targets mouse \
  --save-detection-segments \
  --detection-segment-output-dir runs/realtime/side_cam
```

Each camera worker publishes its `camera_id` in frame, detection, and status messages so downstream closed-loop scripts can subscribe over ZeroMQ independently.

```{tip}
**Quick troubleshooting:** If a wireless stream stutters, switch RTSP transport to `TCP`, lower resolution to `640×480` at `15 FPS`, and verify the stream URL opens in VLC or a browser first. See the [Wireless Camera](https://annolid.com/portal/tutorials/realtime_wireless_camera_detection/) and [Multi-Camera](https://annolid.com/portal/tutorials/multi_camera_realtime/) tutorials on the Docs Portal.
```
