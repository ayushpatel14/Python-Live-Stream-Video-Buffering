# Python-Live-Stream-Video-Buffering
A small script to record Real Time Video effectively with features like Past Video Recording,Variable Speed Playback.

## Requirnments
- Python 3
- OpenCV 
- Numpy

## Usage
This script shows live video stream from webcam, if you wish to record the stream press 'r' button, __the recorded video will contain some seconds(x) before the button press and some seconds(y) after the button press__ .After the video is recorded the script will __playback the recoded video some number of time(z) and with variable speed.These values can be configured in the config.txt file.__ Also this recorded video will be saved in Output folder with .mp4 extension. 

## Configuration File-config.txt
This file contains the configuration of the recorded video. Video Recording(buffering) starts X seconds before button press and ends Y seconds after the button press. After Recording the video playback iters for Z times with the Speed 'Speed'.
