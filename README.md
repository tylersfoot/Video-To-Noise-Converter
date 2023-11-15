# Video-To-Noise-Converter
By tylersfoot
## Overview
I saw this effect on YouTube [link] and I wanted to recreate it. Basically, this script converts a video to 1-bit color (pure black or white), then generates a random noise image, and inverts the noise based on the brightness of the image. This creates an effect where, when paused, looks like just noise, but when playing, you can see outlines in the video.
## Examples
(todo)
## Installation/Usage
- Download and install [Python](https://www.python.org/downloads/).
- Download the [latest release](https://github.com/tylersfoot/Video-To-Noise-Converter/releases) and extract the zip file.
- Install the required packages using `python3 pip install requirements.txt` (I would recommend making a venv)
- Make sure your video is an mp4. If not, you can easily convert it using [this site](https://cloudconvert.com).
- Rename your input video to `input.mp4` and put it inside the `videos` folder.
- Run `main.py`. Progress on the conversion will be shown in the console.
- The converted video will be in the `videos` folder named `output.mp4`.
