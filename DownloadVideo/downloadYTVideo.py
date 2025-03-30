#!/usr/bin/python3
from pytubefix import YouTube
from pytubefix.cli import on_progress
import sys

# Check if the link provided is a valid YouTube video Link
def valid_video(link):
    try:
        video = YouTube(link, on_progress_callback=on_progress)
        return True
    except:
        return False

# main function
def main():
    # get the YT video link
    if len(sys.argv) != 2:
        link = input("Enter video link: ").strip()
    else:
        link = sys.argv[1]
        
    

    yt = valid_video(link)
    
    # Ask user if they got the right video
    print("Video Title:", yt.title)
    ans = input("Is that the video you want to download?(Y/N) ").upper().strip()
    while ans not in "YN":
        print("Error! Enter either Y or N")
        ans = input("Is that the video you want to download?(Y/N) ").upper().strip()
    if ans == 'N':
        print("Thanks for confirming, Download stopped!")
        return 0
    

    ys = yt.streams.get_highest_resolution()
    ys.download()


# Call main
if __name__ == "__main__":
    main()
