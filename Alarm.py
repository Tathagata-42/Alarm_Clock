# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 10:49:02 2021

@author: Tathagata Banerjee
"""

import time
import webbrowser
import random
import os

#To check if the user has the YT.txt file is in the same place as Alarm.py


if os.path.isfile("YT.txt")==False:
    print("ERROR:YT.txt file not present.Creating file...")
    flags=os.O_CREAT | os.O_EXCL | os.O_WRONLY ##WR-write only EXCL-error check
    filecreate=os.open("YT.txt",flags)
    with os.fdopen(fisierCreat,'w')as fileCreated:
        fileCreated.write("https://youtu.be/BZg8BhBWyo8")
        
        
#The User can set the time they want to wake up.
# The String the user puts in must be the same as the example to work.
        
print ("What time do you want to wake up?")
print ("Use this form.\nExample: 06:30")
Alarm = input("> ")


#I first need to state the Time variable so it's usable in the while-loop

Time =time.strftime("%H:%M") #converts datetime object to strings

#This opens the text file with the youtube links

with open("YT.txt") as f:
    content=f.readlines()#the urls are stored in the content variable
    
    
while Time!=Alarm:
    print ("The time is "+Time) ##When the Time does not equal the Alarm time string given above,
    #print the time
    
    #Restating the Time variable allows the time to refresh
	#When I tried keeping the variable outside of the loop it just repeated the inital time
    
    Time = time.strftime("%H:%M")
    
    
    #This keeps the loop from flooding the command line with updates of the time
    time.sleep(10)
    
if Time==Alarm:
    print("Time to wake up!")
    
    #from the variable content, a random link is chosen and then that link is stored in random_video variable
    
    random_video =random.choice(content)
    
    #Using the webbrowser library, it opens this youtube video link
    
    webbrowser.open(random_video)
    
        
