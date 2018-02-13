import time
from pygame import joystick
import pygame
import RPi.GPIO as GPIO
import math
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
def gpio(x,y):
    X = (math.fabs(x)/255)*100
    Y = (math.fabs(y)/255)*100
    GPIO.PWM(18,X)
    GPIO.PWM(13,Y)

def frequency(x,y):
	
joystick.init()
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
    print(x,y,z,q)

def move(x,y):
	if x>0:
		#insert three
	else:
		#insert four
 #Set the duty cycle to the required value
 #Set the frequency 







