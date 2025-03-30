# YouTube Video Downloader (Flask App)

This project provides a simple Flask web application that allows users to download YouTube videos easily using the `pytubefix` library.

## Prerequisites
Ensure you have the following installed:
- Python 3.x (Recommended: 3.8 or later)
- `pip` (Python package manager)
- Virtual environment (Optional, but recommended)
- FFmpeg (For handling video/audio formats, required for some downloads)

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/jeff4444/Python_automation_projects.git
cd Python_automation_projects/DownloadVideo
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Flask App

### 1. Start the Flask Server
```sh
python app.py
```

### 2. Access the Web Interface
Open your browser and go to:
```
http://127.0.0.1:5000
```

## Downloading a YouTube Video via the Web App
1. Open the Flask app in your browser.
2. Enter the YouTube video URL in the input field.
3. Click the **Download** button.
4. The video will be processed and downloaded to the `DownloadVideo/` folder.

## Downloading a Video Using the CLI
If you prefer using the command line, you can run the script directly:
```sh
python VideoDownloader.py video_url
```
Replace `video_url` with the actual video url.
