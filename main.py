import pygame

from window import *

FPS = 60

def main():
  clock = pygame.time.Clock()
  run = True
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    draw_window()
  pygame.quit()

if __name__ == '__main__':
  main()
