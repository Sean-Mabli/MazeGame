import pygame
import numpy as np

Display = pygame.display.set_mode([500, 500])
Screen = 'end'

PlayerX = 0
PlayerY = 0

pygame.init()

done = False

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    if(Screen == 'start'):
      Display.fill((0, 0, 0))
      StartButton = pygame.draw.rect(Display, (255, 255, 255), (150, 300, 200, 60),  2)
      Display.blit(pygame.font.SysFont("Raleway", 70).render("Complete The Maze", 1, (255, 255, 255)), (15, 200))
      Display.blit(pygame.font.SysFont("Raleway", 40).render("Start Game", 1, (255, 255, 255)), (174, 317))

      if(pygame.mouse.get_pressed()[0] == True and StartButton.collidepoint(pygame.mouse.get_pos())):
        Screen = 'game'
    if(Screen == 'game'):
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          PlayerX -= 1
        if event.key == pygame.K_RIGHT:
          PlayerX += 1
        if event.key == pygame.K_UP:
          PlayerY -= 1
        if event.key == pygame.K_DOWN:
          PlayerY += 1

      Display.fill((0, 0, 0))

      Wall = np.ones((4, int(500 / 20), int(500 / 20)))
      VisitedBoxes = np.ones((500, 500))

      for i in range(int(500 / 20)):
        for j in range(int(500 / 20)):
          if (Wall[0, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20, j * 20), (i * 20, j * 20 + 20))
          if (Wall[1, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20, j * 20 + 20), (i * 20 + 20, j * 20 + 20))
          if (Wall[2, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20 + 20, j * 20 + 20), (i * 20 + 20, j * 20))
          if (Wall[3, i, j] == 1):
            pygame.draw.line(Display, (255, 255, 255), (i * 20 + 20, j * 20), (i * 20, j * 20))
    if(Screen == 'end'):
      Display.fill((0, 0, 0))
      StartButton = pygame.draw.rect(Display, (255, 255, 255), (150, 300, 200, 60),  2)
      Display.blit(pygame.font.SysFont("Raleway", 70).render("Game Over", 1, (255, 255, 255)), (115, 200))
      Display.blit(pygame.font.SysFont("Raleway", 40).render("Play Again", 1, (255, 255, 255)), (180, 317))

      if(pygame.mouse.get_pressed()[0] == True and StartButton.collidepoint(pygame.mouse.get_pos())):
        Screen = 'game'

    pygame.display.flip()
pygame.quit()