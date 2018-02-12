import pygame

pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# Prints the joystick's name
JoyName = pygame.joystick.Joystick(0).get_name()
print ("Name of the joystick:")
print (JoyName)
# Gets the number of axes
JoyAx = pygame.joystick.Joystick(0).get_numaxes()
print ("Number of axis:")
print (JoyAx)

# Prints the values for axis0
while True:
        pygame.event.pump()
        print (pygame.joystick.Joystick(0).get_axis(0))
