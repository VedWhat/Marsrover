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

while 1:
    pygame.event.pump()
    x=j.get_axis(0)*255
    y=j.get_axis(1)*(-255)
   
    if y==-0 :
        y=-y

    print(x,y)

    if x>0 :
        w=(x/255)*100
        p.ChangeDutyCycle(w)
        q.ChangeDutyCycle(w)
        r.ChangeDutyCycle(0)
        s.ChangeDutyCycle(0)
        
    

    if x<0 :
        w=math.fabs((x/255)*100)
        p.ChangeDutyCycle(w)
        q.ChangeDutyCycle(w)
        r.ChangeDutyCycle(0)
        s.ChangeDutyCycle(0)
        
    if y<0 :
        a=math.fabs((y/255)*100)
        
        p.ChangeDutyCycle(0)
        q.ChangeDutyCycle(0)
        r.ChangeDutyCycle(a)
        s.ChangeDutyCycle(a)

    if y>0 :
        a=(y/255)*100

        p.ChangeDutyCycle(0)
        q.ChangeDutyCycle(0)
        r.ChangeDutyCycle(a)
        s.ChangeDutyCycle(a)

       

    if x==0:
        p.ChangeDutyCycle(0)
    if y==0:
        r.ChangeDutyCycle(0)
        
      
    
    

