from pathlib import Path
from PIL import Image, ImageDraw
import math

ROOT = Path(__file__).parent
OUTPUT = ROOT / "sample-test.gif"
SIZE = 256
FPS = 12
FRAME_COUNT = 48

frames = []
for index in range(FRAME_COUNT):
    progress = index / (FRAME_COUNT - 1)
    image = Image.new("RGB", (SIZE, SIZE), "black")
    draw = ImageDraw.Draw(image)

    square_x = round(12 + progress * 180)
    square_y = round(35 + 24 * math.sin(progress * math.pi * 4))
    draw.rectangle(
        (square_x, square_y, square_x + 52, square_y + 52),
        fill="white",
    )

    circle_x = round(220 - progress * 184)
    circle_y = round(178 + 22 * math.sin(progress * math.pi * 3))
    draw.ellipse(
        (circle_x - 25, circle_y - 25, circle_x + 25, circle_y + 25),
        fill="white",
    )

    line_offset = round((index * 8) % (SIZE + 80)) - 40
    draw.line(
        (line_offset, SIZE, line_offset + 100, 0),
        fill="white",
        width=7,
    )

    frames.append(image)

frames[0].save(
    OUTPUT,
    save_all=True,
    append_images=frames[1:],
    duration=round(1000 / FPS),
    loop=0,
    optimize=True,
    disposal=2,
)

print(OUTPUT)
