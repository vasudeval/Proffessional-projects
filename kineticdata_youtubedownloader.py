#!/usr/bin/env python
# coding: utf-8

# In[1]:
#Author : vasudeva


import pytube
import skvideo
import moviepy
import moviepy.editor as mp
import skvideo.io 
from pytube import YouTube
import os
import pandas as pd
import numpy as np


# In[2]:


base_link="https://www.youtube.com/watch?v="
file="/home/vasudevarao/project1/data/train.csv"
dest_path_vid='/home/vasudevarao/project1/data/train/pullups/'

#buffer_path='/home/vasudevarao/project1/data/buffer/'
lab='pull ups'
data=pd.read_csv(file)
index_list=[]
label_list=[]
link_list=[]
time_list=[]
for i,j in data.iterrows():
    index_list.append(i)
    
    label_list.append(j[0])
    link_list.append(base_link+j[1])
    time_list.append((j[2],j[3]))


# In[3]:


print(len(time_list))


# In[ ]:



for i in index_list:
    buffer_path='/home/vasudevarao/project1/data/buffer/'
    
    if label_list[i]==lab:
        #print(i)
        #bf=buffer_path+str(i)+"/"
        try:
            yt=YouTube(link_list[i])
            print(i,link_list[i],(int(time_list[i][0]),int(time_list[i][1]-1)))
            yt.streams.get_highest_resolution().download(buffer_path+str(i)+"/")
            for f in os.listdir(buffer_path+str(i)+"/"):
                video=f
            #print(video)
            if yt.length>=int(time_list[i][1]-1):
                vid=mp.VideoFileClip(buffer_path+str(i)+"/"+video)
                clip=vid.subclip(time_list[i][0],time_list[i][1]-1)
                clip.write_videofile(dest_path_vid+str(i)+".mp4")
        except:
            pass
        
    


# In[ ]:




