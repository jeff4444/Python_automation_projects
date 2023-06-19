#!/usr/bin/python3
from pytube import YouTube
import sys
import os

# Check if the link provided is a valid YouTube video Link
def valid_link(link):
    try:
        video = YouTube(link)
        return True
    except:
        return False

# requests choice of resolution
def request_res(resolutions):
    resolution = int(input("Select the number curresponding to your download quality: ").strip())
    while resolution not in list(range(1, len(resolutions) + 1)):
        print("Invalid option chosen")
        resolution = int(input("Select the number curresponding to your download quality: ").strip())
    return resolution

# main function
def main():
    # get the YT video link
    if len(sys.argv) != 2:
        link = input("Enter video link: ").strip()
    else:
        link = sys.argv[1]

    # Checks if link is valid
    if not valid_link(link):
        print("Video not found")
        return 0
    path = os.getcwd()
    video = YouTube(link)

    # Ask user if they got the right video
    print("Video Title:", video.title)
    ans = input("Is that the video you want to download?(Y/N) ").upper().strip()
    while ans not in "YN":
        print("Error! Enter either Y or N")
        ans = input("Is that the video you want to download?(Y/N) ").upper().strip()
    if ans == 'N':
        print("Thanks for confirming, Download stopped!")
        return 0

    # Gets the different streams of the video (Various resolutions)
    video_streams = video.streams.filter(progressive=True)
    resolutions = [stream.resolution for stream in video_streams]

    print("Available resolutions: ")
    for i, res in enumerate(resolutions):
        print(f'{i + 1}: {res}', end='\t')
    print()

    # Gets user choice of resolution
    resolution = request_res(resolutions)
    video_stream = video_streams.get_by_resolution(resolutions[resolution - 1])
    while video_stream is None:
        print("There was an error in getting your required resolution. Please choose another resolution!")
        resolution = request_res(resolutions)
        video_stream = video_streams.get_by_resolution(resolutions[resolution - 1])

    # Gets the path to download the video
    ans = input("Do you want to download in this directory?(Y/N) ").upper().strip()
    while ans not in "YN":
        print("Error! Enter either Y or N")
        ans = input("Do you want to download in this directory?(Y/N) ").upper().strip()
    if ans == 'N':
        path = input("Enter absolute path to download directory: ").strip()
        while not os.path.isdir(path):
            print("Not a valid path")
            path = input("Enter absolute path to download directory: ").strip()

    # Download video
    print("Downloading...")
    video_stream.download(path)
    print("Video downloaded, Enjoy")


# Call main
if __name__ == "__main__":
    main()
