from pytube import Playlist, YouTube
import os
import sys

PATH = "download"
playlist = Playlist(input("URL: "))

try:
    os.mkdir(PATH)
except:
    pass

print(f"Downloading: {playlist.title}")
for x in playlist.video:
    video = x.streams.filter(only_audio=True).first()
    output = video.download(output_path=PATH)
    print(video.title)