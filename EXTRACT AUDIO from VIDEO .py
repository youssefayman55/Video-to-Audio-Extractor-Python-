# pip install moviepy library

# import VideoFileClip function from moviepy library
from moviepy import VideoFileClip

# read the video from video file using VideoFileClip function
cvt_video = VideoFileClip("lv_7473264955412827453_20250224092621.mp4")

# extract audio from the video file (cvt_video)
ext_audio = cvt_video.audio

# save the extracted audio in new file name with new extention (Audio_Extracted.mp3) 
ext_audio.write_audiofile("Audio_Extracted2.mp3")