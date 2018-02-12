import time
from pygame import joystick
import pygame

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
    x=j.get_axis(0)
    y=j.get_axis(1)	
    print(j.get_axis(0),j.get_axis(1))
    
    
