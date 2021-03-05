'''
PART B - Display videos from the video analysis folder
'''
import cv2 
import numpy as np 
   
#ead from input file 
#video = cv2.VideoCapture('/Users/jigyasasingh/Desktop/CSCI 731/assign 1/Toddler rescuing twins from dresser falling Full Video.mp4') 
video = cv2.VideoCapture('/Users/jigyasasingh/Desktop/CSCI 731/assign 1/08390005_road_stripes.AVI') 
#video = cv2.VideoCapture('/Users/jigyasasingh/Desktop/CSCI 731/assign 1/diving_video_far__board_477E38120CAF.MOV') 
#video = cv2.VideoCapture('/Users/jigyasasingh/Desktop/CSCI 731/assign 1/diving_video_far__board_53E7B76AF195.MOV') 
 
if (video.isOpened()== False):  
  print("Error opening video  file") 
   
# Read until video is completed 
while(video.isOpened()): 
  ret, frame = video.read() 
  if ret == True: 
    # Display the resulting frame 
    cv2.imshow('Video', frame) 
    if cv2.waitKey(1) == ord('0'): 
      break
video.release() 

# Closes all the frames 
cv2.destroyAllWindows() 