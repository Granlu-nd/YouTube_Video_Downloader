from operator import imod
from pytube import YouTube 
from sys import argv
import time

file1 = open("Test_Text.txt","r+") 
print(file1.read())

time.sleep(3)

link = argv[1]
yt = YouTube(link)

a = input("Would you like to see the video stats?")
yes = "yes"
no = "no"

if a == yes:
    print("Video Title:" , yt.title)
    print("Views:", yt.views)
    print("Creator:", yt.author)
    print("Video length:", yt.length,"seconds")
    print("Video Keywords:", yt.keywords)
else: 
    print("ok")

d = input("Would you like to download the video?")

if d == yes:
    
    folder = input("Please add the folder path where you would like to download the video.")
    time.sleep(2)
    yd = yt.streams.get_highest_resolution()
    yd.download(folder)
    
else:
    print("Ok! Have a good day.")

    






