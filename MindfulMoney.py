import pygame
pygame.init()
width = 500
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.flip()

open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

pygame.quit()
quit() 