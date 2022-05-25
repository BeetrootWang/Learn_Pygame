# A naive program that import the pygame library and gives a black window
import pygame

def main():
    # initialize pygame module
    pygame.init()

    # Set logo and caption
    icon = pygame.image.load('./images/icon.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('set caption here')

    # Create a screen of size 360x360
    screen = pygame.display.set_mode((1000,1000))

    # Define a variable <running> that control the main loop
    running = True

    # Main loop
    while running:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == '__main__':
    main()