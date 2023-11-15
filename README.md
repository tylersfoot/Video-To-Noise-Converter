# Video-To-Noise-Converter
By tylersfoot

## Overview
I saw this effect on YouTube [link] and I wanted to recreate it. Basically, this script converts a video to 1-bit color (pure black or white), then generates a random noise image, and inverts the noise based on the brightness of the image. This creates an effect where, when paused, looks like just noise, but when playing, you can see outlines in the video.

## Example
Original Bad Apple animation:
https://github.com/tylersfoot/Video-To-Noise-Converter/assets/93095330/a8625c11-36fc-49b6-9fdf-b99a665560b2

Converted Bad Apple animation:
https://github.com/tylersfoot/Video-To-Noise-Converter/assets/93095330/a9eb2f27-1b8a-4dae-913f-2ee6406a4a1b

## Installation/Usage
- Download and install [Python](https://www.python.org/downloads/).
- Download the [latest release](https://github.com/tylersfoot/Video-To-Noise-Converter/releases) and extract the zip file.
- Navigate to the directory in a terminal and install the required packages using `py -m pip install -r requirements.txt`
- Make sure your video is an mp4. If not, you can easily convert it using [this site](https://cloudconvert.com).
- Rename your input video to `input.mp4` and put it in the folder.
- Run `py main.py`. Progress on the conversion will be shown in the console.
- The converted video will be named `output.mp4`.
