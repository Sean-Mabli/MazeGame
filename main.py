import pygame
import numpy as np
import sys

Display = pygame.display.set_mode([500, 500])
Screen = 'game'

PlayerX = 0
PlayerY = 0

pygame.init()
pygame.display.set_caption('Maze Game - Sean Mabli')

for event in pygame.event.get():
  if event.type == pygame.QUIT:
    pygame.quit()
    sys.exit()
  if(Screen == 'start'):
    Display.fill((0, 0, 0))
    button = pygame.draw.rect(Display, (255, 255, 255), (150, 300, 200, 60),  2)
    Display.blit(pygame.font.SysFont("Raleway", 70).render("Complete The Maze", 1,(255, 255, 255)), (15, 175))
    Display.blit(pygame.font.SysFont("Raleway", 40).render("Start Game", 1, (255, 255,255)), (174, 317))
    if button.collidepoint(pygame.mouse.get_pos()):
      print(".")
  if(Screen == 'game'):
    '''
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        PlayerX -= 1
      if event.key == pygame.K_RIGHT:
        PlayerX += 1
      if event.key == pygame.K_UP:
        PlayerY -= 1
      if event.key == pygame.K_DOWN:
        PlayerY += 1
    '''
    Display.fill((0, 0, 0))
    Wall = np.ones((4, int(500 / 20), int(500 / 20)))
    for i in range(int(500 / 20)):
      for j in range(int(500 / 20)):
        if (Wall[0, i, j] == 1):
          pygame.draw.line(Display, (255, 255, 255), (i * 20, j * 20), (i * 20, j * 20 + 20))
        if (Wall[1, i, j] == 1):
          pygame.draw.line(Display, (255, 255, 255), (i * 20, j * 20 + 20), (i * 20 +20, j * 20 + 20))
        if (Wall[2, i, j] == 1):
          pygame.draw.line(Display, (255, 255, 255), (i * 20 + 20, j * 20 + 20), (i *20 + 20, j * 20))
        if (Wall[3, i, j] == 1):
          pygame.draw.line(Display, (255, 255, 255), (i * 20 + 20, j * 20), (i * 20, j* 20))
  pygame.display.flip()