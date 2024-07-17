# Livestream Network Compatibility Check

This Python script helps you determine the optimal livestream settings based on your internet speed and hardware specifications. It provides recommended settings for platforms like YouTube and Facebook.

## Features

- **Check Internet Speed**: Measures upload speed to determine available bitrate.
- **Check Hardware Specifications**: Assesses CPU usage, RAM, and GPU.
- **Determine Streaming Requirements**: Provides minimum and recommended bitrates for YouTube and Facebook.
- **Calculate Best Settings**: Suggests the best resolution, FPS, video bitrate, audio bitrate, and audio sample rate based on your setup.
- **Graphical User Interface (GUI)**: Simple interface using Tkinter for easy interaction.

## Requirements

- Python 3.x
- speedtest-cli
- psutil
- GPUtil
- Tkinter (included in standard Python library)

## Installation

1. Install the required Python packages:
   ```bash
   pip install speedtest-cli psutil gputil
   ```

2. Save the script to a file, for example, `app.py`.

## Usage

1. Run the script:
   ```bash
   python app.py
   ```

2. Click the "Check Settings" button in the GUI to start the analysis.

## Code Explanation

### Functions

- **check_internet_speed()**: Uses `speedtest` to measure upload speed in Mbps.
- **check_hardware()**: Uses `psutil` to get CPU usage and total RAM, and `GPUtil` to get GPU information.
- **get_streaming_requirements()**: Returns the minimum, maximum, and recommended bitrates for YouTube and Facebook.
- **calculate_best_settings()**: Calculates the best streaming settings based on upload speed and hardware.
- **check_settings_thread()**: Runs the internet speed and hardware checks, and calculates the best settings.
- **update_results()**: Updates the GUI with the results.
- **start_check()**: Disables the button and starts the checking thread.

### GUI

- Created using `tkinter` and `ttk`.
- Contains a button to start the checking process and a text widget to display results.

## Example Output

When you run the script and click "Check Settings", you will see output similar to this:

```
Upload Speed: 29.46 Mbps

Hardware:
CPU Usage: 15%
RAM: 16.00 GB
GPU: NVIDIA GeForce GTX 1060

Streaming Requirements:
YouTube: 1500-12000 kbps (video)
Facebook: 1500-4000 kbps (video)

Best Settings:
Resolution: 1080p
FPS: 60
Video Bitrate: 6000 kbps
Audio Bitrate: 192 kbps
Audio Sample Rate: 48000 Hz
```

This output provides you with the optimal settings for your livestream based on your current internet speed and hardware capabilities.
