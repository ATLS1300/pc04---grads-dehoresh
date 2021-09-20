#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 10:57:36 2021

Art Description: 
    Blue background with White oval and parametric equation inside. Background has multicolored blue diagonals leading to varying waves 
ATLS 1300
Author: Dr. Z
Author: Dover Horesh
Sept 18, 2021
"""


import turtle
import math
import random




t=turtle
r=random
t.colormode(255)

#Make Panel 800x600

Screen= t.Screen()
w = 800 # width of screen
h = 600 # width of screen


Screen.setup(width=w, height=h) 





#Set variable lists
#Fish Color, Eye Color, Wave Color, Background colors

#17
#Line can be many shades of orange, red, purple. green, yellow
DrawC= [(0,127,95),(85,166,48),(128,185,24),(191,210,0),(47,151,193),(160,234,222),(249,214,22)]

#9
#Waves can be shades of blue
WaveC=[(2,62,138), (0,119,182), (0,150,199), (0,180,216), (72,202,228), (144,224,239), (173,232,244), (202,240,248)]

#Background colors shades blue 
BG = [(33,41,92), (27,59,111),(6,90,130),(28,114,147),(56,160,198)]

#Set Scale factor



#Set Background Color Random from list
Screen.bgcolor(random.choice(BG))

#Based on Pseudocode from Rachel Wildeson adapted from Dr. Z's Wave example


#Start making waves
#make turtle for waves
waves = t.Turtle()


#SET VALUES FOR WAVES
#set range for random height of waves
WH = r.randrange(10,30)

# set range for random width of waves
WW= r.randrange(20,50)

#set angles
WA = range(0,360)

#Set start point for diagonals
WSY = (-400)


waves.penup()
waves.goto (-300,WSY)


#Forloop waves
while WSY<350:
        WSY = WSY + (r.randrange(40,80,5)) #random number from 40-80 in steps of 5
       
       
        #Set line thickness variation. Want ends to be tapered?
        waves.pensize(r.randrange(3,6))
        #Set speed
        waves.speed(10)
        
        #WS = (-400,WSY) #Wave Start
        waves.goto (-400,WSY)
        
        waves.pendown()
        
        #Set linecolor to random color from waves color list (iteration)
        waves.pencolor(WaveC[r.randrange(8)])
        
        #SET VALUES FOR WAVES
        #set range for random height of waves
        WH = r.randrange(20,90,5)

        # set range for random width of waves
        WW= r.randrange(30,80,5)
       
        #input Wave equation from DR Z example
        for angle in WA:
           
            
            RAD = math.radians(angle)  # convert from degrees (0-360) to radians (0-2*pi)
            Y = WH * math.sin(RAD) + WW # use the sine function to create a wave
            X = angle # move forward so it makes a wave, not a line
            waves.pendown()
            waves.goto(X,Y)
             
           
   

   


#Make new turtle called Draw
Draw=t.Turtle()

# Set speed 10, think, Random color
Draw.speed(10)
Draw.pensize(2)



#Set pen thickness/speed for oval
t.pensize(2)
t.speed(10)



# Code from Geek Tutorials on how to make an oval. 
t.penup()
t.goto(0, 0)
t.pendown()
t.shape("circle")
t.pencolor("white")
t.fillcolor("white")
t.shapesize(25, 18, 2) # (length, width, outline)


#move pen so it doesn't look out of place
Draw.penup()
Draw.goto(100,0)

#code copied from DR Z's Bean Example and edited
ANGLES = range(0,360) # change this depending on your pattern!
for angle in ANGLES:
    angle = math.radians(angle) # overwrites input to radians (required!)

   


smooth = 5 
scale = 75

ANGLES = range(0,(720 * smooth))

for angle in ANGLES:
  
   #Set linecolor to random color from waves color list (iteration)
    Draw.pencolor(DrawC[r.randrange(7)])
    
    angle = math.radians(angle/(2*smooth))

    x = ((math.cos(angle) - math.cos(80*angle)* math.sin(angle)))*scale
    y = (2 * math.sin(angle) - math.sin(80 * angle)) * scale
 


    Draw.goto (x,y)
    Draw.pendown()

#end turtle
t.done()