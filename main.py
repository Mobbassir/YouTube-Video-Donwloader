#import the package
from pytube import YouTube

function_patterns = [

    r'a\.[A-Z]&&\(b=a\.get\("n"\)\)&&\(b=([^(]+)\(b\)',
]

url = input("Enter Video Url:  ")
my_video = YouTube(url)

print("**********YouTube Title**********")
print(my_video.title)

print("**********YouTube Thumbnail Image**********")
print(my_video.thumbnail_url)

print("**********Download Video**********")

#set stream resolution
# my_video = my_video.streams.get_highest_resolution()
my_video = my_video.streams.get_highest_resolution()

# or my_video = my_video.streams.first()
# for stream in my_video.streams:
#     print(stream)

my_video.download()