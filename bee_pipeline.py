# -*- coding: utf-8 -*-
"""bee_pipeline

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10CWORdP3KNS-_2t_IGHvBJS3Yz6bzLW5
"""

import cv2
import os
import bb_capture
from yaml import safe_load

def get_frame_zero():
    with open('bounding_boxes.ymal','r') as f:
        config=safe_load(f)
        cap=cv2.VideoCapture(config.get('video path'))
        ret,frame=cap.read
    return frame

def capture_bounding_boxes(frame):
    # https://dash.plotly.com/annotations

import os
import deeplabcut
import pathlib

config="/home/jchan/Desktop/BeeInTube-Jose Hernandeaz Campos-2023-04-17/config.yaml"

path="/home/jchan/Desktop/BeeInTube-Jose Hernandeaz Campos-2023-04-17/videos/"

files=["1_12_R_230214155032.avi","1_43_R_230214154432.avi", "2_11_R_230214180000.avi", "3_11_R_230214190000.avi",
      "3_12_R_230214170000.avi", "4_11_R_230214155032.avi", "4_11_R_230214200000.avi", "5_11_R_230214170000.avi",
      "5_11_R_230214210000.avi", "13_11_R_230215050000.avi", "14_11_R_230215060000.avi", "15_11_R_230215070000.avi",
      "16_11_R_230215080000.avi", "17_11_R_230215090000.avi"]

videos=[]

for f in files:
    videos.append(path+f)

videotype='.avi'

gputouse=0

save_as_csv=True

auto_track=False

deeplabcut.analyze_videos(config=config,videos=videos,videotype=videotype,gputouse=gputouse,save_as_csv=save_as_csv,auto_track=auto_track)

