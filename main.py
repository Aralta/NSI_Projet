import pygame
from grid import*


pygame.init()
pygame.display.set_caption('DOGS ADVENTURE')
screen = pygame.display.set_mode((DISPLAYWEIDTH,DISPLAYHEIGHT))




launched = True
while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            screen.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
    pygame.display.update()

