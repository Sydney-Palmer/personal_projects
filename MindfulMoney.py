import pygame

#Initalize Screen and Set Background Green
pygame.init()
width = 800
height = 500
screen = pygame.display.set_mode((width, height))
green_background = (133,187,101)
screen.fill(green_background)
pygame.display.flip()

#Create Title
title_color = (1,40,26)
title_font = pygame.font.SysFont('Arial', 36)
title = title_font.render("Mindful Money", True,title_color)
screen.blit(title, (300,200))
pygame.display.flip()





open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

pygame.quit()
quit() 