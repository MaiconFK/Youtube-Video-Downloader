#Youtube Video Downloader
from pytube import YouTube
from tkinter import *

Base_youtube_url = ()

while True:
    url = input("Please insert your url from a youtube video")

    if url.lower().startswith("https://www.youtube.com"):
        break
    else:
     print("ERROR: you need to put a Youtube URL.")

def on_download_progress(stream ,chunk , bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percentage = bytes_downloaded * 100/ stream.filesize

    print(f"downloading...{int(percentage)}")

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)
print("Title: " , youtube_video.title)
print("Number of views:" , youtube_video.views)

stream = youtube_video.streams.get_highest_resolution()
print("Loading...")
stream.download()
print("Ok")


