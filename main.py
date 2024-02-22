from pytube import YouTube
import os
from sys import argv

link = argv[1]                 #  get the link from the command line
yt = YouTube(link)             #  create a YouTube object

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")

yd = yt.streams.get_highest_resolution()  #  get the highest resolution video

print("Downloading... ", yt.title)
yd.download(r"C:\Users\Administrator\Desktop\100dayscode\Youtube-video-downloader")                   #  download the video



# def download_video(url, path):
#     yt = YouTube(url)
#     yt.