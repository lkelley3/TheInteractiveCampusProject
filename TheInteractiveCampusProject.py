#Lauren will add comments!
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("The Interactive Campus Project")
    x_coord = 10
    y_coord = 10
    joystick_count = pygame.joystick.get_count()
    avatar1 = pygame.image.load("PicturesICP/avatar1.bmp").convert()
    avatar2 = pygame.image.load("PicturesICP/avatar2.bmp").convert()
    movingImage = []
    movingImage.append(avatar1)
    movingImage.append(avatar2)
    #movingImage = []
    #list(movingImage)
    if joystick_count == 0:
        print("Error, I didn't find any joysticks.")
    else:
        my_joystick = pygame.joystick.Joystick(0)
        my_joystick.init()
        FPS = 10
        fpsClock = pygame.time.Clock()
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    #y = play
    backgroundImage = pygame.image.load("PicturesICP/SpelmanSatelliteImage.bmp").convert()
    #avatarImage = pygame.image.load("avatar.bmp").convert()
    WHITE = (255, 255, 255)
    #avatarImage.set_colorkey(WHITE)#define white
    #avatarx = my_joystick.get_axis(0)
    #avatary = my_joystick.get_axis(1)
    image_index = 0
    counter = 0
    #x = 0
    while True:
        
        #get all events
        #avatarPosition = pygame.mouse.get_pos()
        #avatarPosition = my_joystick
        #x = avatarPosition[0]
        #y = avatarPosition[1]
        avatarx = my_joystick.get_axis(0)
        avatary = my_joystick.get_axis(1)
        x_coord = x_coord + int(avatarx * 10)
        y_coord = y_coord + int(avatary * 10)
        if True == False:
            if my_joystick.get_axis(0) > 0:
                avatarx += 10
                print(avatarx)
                if avatarx > 900: #This is to keep my image inside my window. Erase these lines
                    avatarx = 900 #to allow the image to move freely outside the display.
            if my_joystick.get_axis(0) < 0:
               x_coord -= 10
               if avatarx < 0:
                   avatarx = 0
            if my_joystick.get_axis(1) > 0:
                avatary += 10 
                if avatary > 800:
                    avatary = 800
            if my_joystick.get_axis(1) < 0:
                avatary -= 10 
                if avatary < 0:
                    avatary = 0
        DISPLAYSURF.blit(backgroundImage, [0,0])
        #for x in movingImage:
        DISPLAYSURF.blit(movingImage[image_index], (x_coord, y_coord))
        if counter % 10 == 0:
            image_index += 1
            if image_index == 2:
               image_index = 0
    ##        if (x+1) % 10 == 0:
    ##            image_index + 1 
    ##        if image_index == 4:
    ##            image_index = 0
        
     #   DISPLAYSURF.blit(avatar1, (x_coord, y_coord))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                print("Key Down")
            elif event.type == JOYAXISMOTION:
                print("joystick axis motion")
            elif event.type == JOYBUTTONDOWN:
                print("you pressed the joystick button")
            elif event.type == JOYBUTTONUP:
                print("you released the joystick button")
            
        
        counter += 1
        #update the display
        pygame.display.update()
     #   fpsClock.tick(FPS) 



main()

