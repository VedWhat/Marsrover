import time
from pygame import joystick
import pygame
import math
import RPi.GPIO as IO
#a b
#c d
IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(17,IO.OUT)
IO.setup(18,IO.OUT)
IO.setup(19,IO.OUT)
IO.setup(16,IO.OUT)
a=IO.PWM(17,100)
b=IO.PWM(18,100)
c=IO.PWM(19,100)
d=IO.PWM(16,100)
pygame.display.init()
j=joystick.Joystick(0)
j.init()
print(j.get_name())
print(j.get_init())
c=j.get_numaxes()
print(int(c))
print(j.get_axis(0))
while(1):
    pygame.event.pump()
    x=j.get_axis(0)*255
    y=j.get_axis(1)*(-255)
    z=j.get_axis(2)*255
    q=j.get_axis(3)*(-255)
    if y==-0 :
        y=-y
    if q==-0 :
        q=-q
    print(x,y)
 
if y>0:
    bf=float((y/255)*100)
    af=bf
    a.ChangeDutyCycle(af)
    b.ChangeDutyCycle(bf)
    c.ChangeDutyCycle(0)
    d.ChangeDutyCycle(0)
else:
    cf=float((y/255)*100)
    df=cf
    c.ChangeDutyCycle(cf)
    d.ChangeDutyCycle(df)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)

if x>0:
    af=float((x/255)*100)
    cf=af
    a.ChangeDutyCycle(af)
    b.ChangeDutyCycle(0)
    c.ChangeDutyCycle(cf)
    d.ChangeDutyCycle(0)
else:
    bf=float((x/255)*100)
    df=df
    c.ChangeDutyCycle(0)
    d.ChangeDutyCycle(df)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(bf)
    



