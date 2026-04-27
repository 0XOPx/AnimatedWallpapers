# 🐈 Cat-Powered Wallpaper Engine
A high-performance Python script that injects a video loop directly into the Windows `WorkerW` layer.

## Features
- **60 FPS** smooth playback.
- **Auto-Lock:** Prevents multiple instances from running.
- **Task Scheduler Friendly:** Designed for instant boot-up.
- **Invisible:** No taskbar icon, stays behind desktop icons.

## Requirements
- Python 3.13+
- `pygame`, `opencv-python`, `pywin32`, `numpy`
- Windows 10 or above

## Install Instructions

1. Install Python 3.13 or higher from https://www.python.org/ - after, restart your terminal

2. After Installing Python, I recommend you to get a virtual enviroment. To get one - if you did not add to path - do `py -m venv venv` or if you have it in path - do `python -m venv venv` and after do "venv\Scripts\activate" or in powershell - "./venv\Scripts\activate.ps1"

3. To install the packages - do `pip install -r packages.txt` or if not using venv - it is recommended if Scripts directory is not in PATH to do `py -m pip install -r  packages.txt`

4. Just do `python wallpaper.py` (or `py wallpaper.py`) and you're ready to go!

(If you dont want the hassle, you can go to the releases tab!)

## Contribution

Feel free to fork this!
Just in there - get the original Apache 2.0 License I had, link this repo - and you're good to go!