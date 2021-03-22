"""Virtual Clapperboard
By Al Sweigart al@inventwithpython.com

A virtual clapperboard program for syncing an audio tone with a visual cue on the screen. Written in Python & Pygame."""

__version__ = '0.1.0'


import pygame, time, sys, os
from pygame.locals import MOUSEBUTTONDOWN, QUIT, KEYDOWN, K_ESCAPE

FOLDER_OF_THIS_FILE = os.path.dirname(os.path.abspath(__file__))


def main():
    pygame.init()
    FONT = pygame.font.SysFont('Arial', 50)

    clickMessageSurface = FONT.render('Click to clap.', True, (255, 255, 255))
    tone = pygame.mixer.Sound(os.path.join(FOLDER_OF_THIS_FILE, 'tone300hz.wav'))
    DISPLAYSURF = pygame.display.set_mode((400, 400))

    while True:
        DISPLAYSURF.fill((0, 0, 0)) # fill with black
        clickMessageRect = clickMessageSurface.get_rect()
        DISPLAYSURF.blit(clickMessageSurface, clickMessageRect)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                # Start the clapper.
                tone.play()
                DISPLAYSURF.fill((255, 0, 0))
                pygame.display.update()
                time.sleep(1)
                DISPLAYSURF.fill((0, 0, 0)) # fill with black
                pygame.display.update()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

if __name__ == '__main__':
    main()
