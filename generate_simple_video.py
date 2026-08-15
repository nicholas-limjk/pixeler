from pathlib import Path
import sys

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / ".video-tools"))

import imageio.v2 as imageio
import numpy as np

SIZE = 384
FPS = 12
DURATION = 6
OUTPUT = ROOT / "simple-video.mp4"

writer = imageio.get_writer(
    OUTPUT,
    fps=FPS,
    codec="libx264",
    quality=8,
    pixelformat="yuv420p",
)

for frame_number in range(FPS * DURATION):
    t = frame_number / (FPS * DURATION - 1)
    frame = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)

    # A large square travels left to right and gently bounces vertically.
    square = 72
    x = int(24 + t * (SIZE - square - 48))
    y = int(70 + 45 * np.sin(t * np.pi * 4))
    frame[y:y + square, x:x + square] = 255

    # A circle travels in the opposite direction across the lower half.
    cx = int(SIZE - 55 - t * (SIZE - 110))
    cy = int(275 + 35 * np.sin(t * np.pi * 3))
    radius = 38
    yy, xx = np.ogrid[:SIZE, :SIZE]
    frame[(xx - cx) ** 2 + (yy - cy) ** 2 <= radius ** 2] = 255

    writer.append_data(frame)

writer.close()
print(OUTPUT)
