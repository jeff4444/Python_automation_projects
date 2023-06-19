#!/usr/bin/python3
import os
import shutil
import sys

if (len(sys.argv) < 2):
    maindir = '.'
else:
    if os.path.isdir(sys.argv[1]):
        maindir = sys.argv[1]
    else:
        print("Your entered a non-valid path")
        sys.exit(1)

files = os.listdir(maindir)

file_extensions = {
    ".txt": "Text Files",
    ".doc": "Word Documents",
    ".docx": "Word Documents",
    ".pdf": "PDF Documents",
    ".xlsx": "Excel Spreadsheets",
    ".csv": "CSV Files",
    ".jpg": "JPEG Images",
    ".png": "PNG Images",
    ".gif": "GIF Images",
    ".mp3": "MP3 Audios",
    ".mp4": "MP4 Videos",
    ".zip": "ZIP Archives",
    ".rar": "RAR Archives",
    ".tar": "TAR Archives",
    ".exe": "Executable Files",
    ".py": "Python Scripts",
    ".html": "HTML Files",
    ".css": "CSS Files",
    ".js": "JavaScript Files",
    ".ppt": "PowerPoint Presentations",
    ".pptx": "PowerPoint Presentations",
    ".svg": "Scalable Vector Graphicss",
    ".json": "JSON Files",
    ".xml": "XML Files",
    ".sql": "SQL Scripts",
    ".apk": "Android Packages",
    ".iso": "Disk Images",
    ".avif": "Avif Images",
    ".c": "C files",
    ".cpp": "C++ Files",
    ".md": "Markdown Files",
    ".xls": "Old Excel Spreadsheets",
    ".odt": "OpenDocument Text",
    ".odp": "OpenDocument Presentation",
    ".ods": "OpenDocument Spreadsheet",
    ".wav": "WAV Audio",
    ".avi": "AVI Video",
    ".svgz": "Compressed SVG",
    ".yaml": "YAML File",
    ".ini": "INI File",
    ".bat": "Batch File",
    ".java": "Java Source Code",
    ".psd": "Photoshop Document",
    ".ai": "Adobe Illustrator File",
    ".mov": "QuickTime Video",
    ".key": "Keynote Presentation",
    ".numbers": "Numbers Spreadsheet",
    ".pages": "Pages Document",
    ".tgz": "Compressed Tar Archive",
    "": "None",
    # Add more file extensions and types as needed
}

extensions = set()
for some_file in files:
    if os.path.isfile(maindir + '/' + some_file):
        _, ext = os.path.splitext(some_file)
        extensions.add(ext)

for ext in extensions:
    if ext in list(file_extensions):
        dirname = file_extensions[ext]
    else:
        dirname = ext[1:]
    if os.path.isdir(maindir + "/" + dirname) is False:
        os.mkdir(maindir + '/' + dirname)
    for some_file in files:
        if os.path.isdir(maindir + '/' + some_file):
            continue
        _, file_ext = os.path.splitext(some_file)
        if file_ext == ext:
            shutil.move((maindir + '/' + some_file), (maindir + '/' + dirname))
