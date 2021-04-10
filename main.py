import pygame
import numpy as np
import time
import sys

Display = pygame.display.set_mode([500, 500])
Screen = 'game'

PlayerX = 0
PlayerY = 0

CurrentX = 0
CurrentY = 0

Wall = np.ones((4, int(500 / 20), int(500 / 20)))
VisitedBoxes = np.zeros((500, 500))

pygame.init()

done = False

pygame.display.set_caption('Maze Game - Sean Mabli')

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
      Display.fill((0, 0, 0))

      VisitedBoxes[CurrentX, CurrentY] = 1
      OpenBoxes = np.zeros((4))

      if(VisitedBoxes[CurrentX, CurrentY - 1]  == 0 and CurrentY != 0): # Top
        OpenBoxes[0] = 1
      if(VisitedBoxes[CurrentX + 1, CurrentY]  == 0 and CurrentX != 24): # Right
        OpenBoxes[1] = 1
      if(VisitedBoxes[CurrentX, CurrentY + 1]  == 0 and CurrentY != 24): # Down
        OpenBoxes[2] = 1
      if(VisitedBoxes[CurrentX - 1, CurrentY]  == 0 and CurrentX != 0): # Right
        OpenBoxes[3] = 1

      Random = np.random.randint(0, 4)
      while (OpenBoxes[Random] != 1 and np.sum(OpenBoxes) != 0):
        Random = np.random.randint(0, 4)
      
      print(sum(OpenBoxes))

      if(sum(OpenBoxes) == 0):
        while True:
          w = 0

      if(Random == 0):
        CurrentY -= 1
      elif(Random == 1):
        CurrentX += 1
      elif(Random == 2):
        CurrentY += 1
      elif(Random == 3):
        CurrentX -= 1

      for i in range(int(500 / 20)):
        for j in range(int(500 / 20)):
          if(VisitedBoxes[i, j] == 1):
            pygame.draw.rect(Display, (255, 255, 255), (i * 20, j * 20, 20, 20))
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