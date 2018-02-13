import time
from pygame import joystick
import pygame
import math
<<<<<<< HEAD
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
=======
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
>>>>>>> 4f2b34b11da6763f9085120e63d3fd86c652a247
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
<<<<<<< HEAD
#    print(x,y,z,q)
    gpio(x,y)
=======
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
    



>>>>>>> 4f2b34b11da6763f9085120e63d3fd86c652a247
