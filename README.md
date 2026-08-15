# 128×128 Video Pixeler

A dependency-free browser tool that converts up to 10 seconds of a video or animated GIF chain into a true 128×128, black-and-white WebM using a media-guided Conway's Game of Life simulation.

## Run

Open `index.html` in Chrome or Edge, choose a video or one to four GIFs, adjust the controls, and click **Export WebM**. Multiple GIFs are chained in selection order, then time-fitted so the complete chain appears within the 10-second export.

The complete GIF chain is time-fitted into the 10-second output, so later GIFs are not cut off. **Export 4-Way Comparison** creates a synchronized 2×2 video showing guidance values of 0%, 25%, 75%, and 100%.

Use **Try Sample Flower Video** to test with the included public-domain MDN flower clip.

Each output frame advances Conway's Game of Life by one generation. The **Video guidance** control sets the probability that a cell which differs from the source video will be pulled back toward it. At 0% the video is only the initial seed; at 100% the output follows the thresholded video exactly.

**Auto threshold** is enabled by default. It combines brightness with local edge contrast, preserving outlines and internal features instead of producing flat silhouettes. **Shape density** controls the percentage of cells the algorithm aims to keep alive; 25–35% usually creates the most interesting Life patterns. Disable auto threshold to use the brightness slider manually.

**Auto-tune shape density** measures edge complexity on every frame. Simple frames receive a denser cell seed so they remain active; highly detailed frames receive a sparser seed to avoid collapsing into visual noise. The value is smoothed over time to prevent flicker.

The output contains exactly 16,384 cells per frame. The enlarged preview uses nearest-neighbor rendering so each cell stays sharp.
