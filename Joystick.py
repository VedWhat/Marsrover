import time
from pygame import joystick
import pygame
import RPi.GPIO as GPIO
import math
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
p=GPIO.PWM(12,50)
q=GPIO.PWM(33,50)
p.start(0)
q.start(0)
def gpio(x,y):
    X = int((math.fabs(x)/255)*100)
    Y = int((math.fabs(y)/255)*100)
    p.ChangeDutyCycle(X)
    q.ChangeDutyCycle(Y)

joystick.init()
#pygame.display.init()
j=joystick.Joystick(0)
j.init()
print(j.get_name())
print(j.get_init())
c=j.get_numaxes()
print(int(c))
print(j.get_axis(0))
while(1):
#    pygame.event.pump()
    x=j.get_axis(0)*255
    y=j.get_axis(1)*(-255)
    z=j.get_axis(2)*255
    q=j.get_axis(3)*(-255)
    if y==-0 :
        y=-y
    if q==-0 :
        q=-q
#    print(x,y,z,q)
    gpio(x,y)
