import pygame

# WIDTH, HEIGHT = 800, 600
# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

from window import *

def main():
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    draw_window()
  pygame.quit()

if __name__ == '__main__':
  main()
