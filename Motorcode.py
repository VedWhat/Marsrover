import RPi.GPIO as IO          
from pygame import joystick
import pygame
import time
import math

joystick.init()
pygame.display.init()
j=joystick.Joystick(0)
j.init()

IO.setwarnings(False)          

IO.setmode (IO.BCM)         
IO.setup(12,IO.OUT)
IO.setup(13,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(19,IO.OUT)


p = IO.PWM(12,500)
q = IO.PWM(13,500)
r = IO.PWM(18,500)
s = IO.PWM(19,500)


p.start(0)
q.start(0)
r.start(0)
s.start(0)  
def mapfn(x,in_min,in_max,out_min,out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
def first(x,y):
    if x<y:
        #second octant
        left=y
        right=mapfn(x,0,y,left,0)
    else:
        #first octant
        left =  mapfn(y,0,x,0,255)
        right = mapfn(x,y,255,0,255)
    return left,right    
def second(x,y):
    if y>-x:
        #third octant
        right=y
        left=mapfn(-x,0,y,right,0)
    else:
        #fourth octant
        right=mapfn(y,0,-x,0,255)
        left=mapfn(-x,y,255,0,255)
    return left,right    
def third(x,y):
    if -y>-x:
        #sixth octant
        right = mapfn(x,y,255,0,255)
        left =mapfn(y,0,x,0,right)
    else:
        #fifth octant
        left= mapfn(-y,0,255,0,255)
        right =mapfn(-x,y,255,0,255)
    return left,right   
        
def fourth(x,y):
    if -y>-x:
        #seventh octant
        right=-y
        left=mapfn(-x,0,-y,right,0)
    else:
        #eight octant
        right =  mapfn(-y,0,x,0,255)
        left = mapfn(x,-y,255,0,255)
    return left,right   
while 1:
    pygame.event.pump()
    x=j.get_axis(0)*255
    y=j.get_axis(1)*(-255)
   
    if y==-0 :
        y=-y

    #print(x,y)


    if y>0:
        if x>0:
            left,right=first(x,y)
        else:
            left,right=second(x,y)
    else:
        if x>0:
            left,right=fourth(x,y)
        else:
            left,right=third(x,y)
    print(left,right)        
