# A naive program that import the pygame library and gives a black window
# Reference:
#   https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html
import pygame
import numpy as np

def main():
    # initialize pygame module
    pygame.init()

    # Set logo and caption
    icon = pygame.image.load('./images/icon.png')
    icon.set_colorkey((255,255,255))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Bad day for Beetroot")

    # Create a screen of size 1000x1000
    screen = pygame.display.set_mode((1000,1000))

    # Define a variable <running> that control the main loop
    running = True

    # position for the top left corner of an image to be displayed on the screen
    x_axis = 50
    y_axis = 600
    sgn_x = 1
    sgn_y = 1
    speed = .1
    cnt = 0

    # Main loop
    while running:
        # event handling
        for event in pygame.event.get():
            # Stop the program when the user click on the close button
            if event.type == pygame.QUIT:
                running = False
        # update the screen
        x_axis = max(min(x_axis+sgn_x*speed, 900),50)
        y_axis = max(min(y_axis+sgn_y*speed, 900),50)
        if x_axis>=900 or x_axis<=50:
            sgn_x = -sgn_x
        if y_axis>=900 or y_axis<=50:
            sgn_y = -sgn_y

        cnt = cnt + 1
        if cnt % 100==0:
            speed = np.random.exponential()*.5
            sgn_x = (-1)**np.random.randint(0,2)
            sgn_y = (-1)**np.random.randint(0,2)
            screen.fill((0,0,0))
        # update screen
        screen.blit(icon,(x_axis, y_axis))
        pygame.display.flip()

if __name__ == '__main__':
    main()