import pygame

def handle_alien_shots(
  laser: pygame.Rect,
  alien_shots: list,
  laser_image: list,
  shields: list,
  shield_images: list
):
  for shot in alien_shots:
    shot.y += 7
    if laser.colliderect(shot):
      laser_image[0] += 7
      if shot in alien_shots:
        alien_shots.remove(shot)

    for idx, shield in enumerate(shields):
      if shield != 0 and shield.colliderect(shot):
        if shield_images[idx] == 5:
          shields[idx] = 0
        shield_images[idx] += 1
        if shot in alien_shots:
          alien_shots.remove(shot)
