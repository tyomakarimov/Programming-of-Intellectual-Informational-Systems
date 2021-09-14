import pygame

def handle_asteroids(
  laser: pygame.Rect,
  asteroids: list,
  laser_image: list,
  shields: list,
  shield_images: list
):
  for asteroid in asteroids:
    asteroid.y += 5
    if laser.colliderect(asteroid):
      laser_image[0] += 1
      if asteroid in asteroids:
        asteroids.remove(asteroid)

    for idx, shield in enumerate(shields):
      if shield != 0 and shield.colliderect(asteroid):
        if shield_images[idx] == 5:
          shields[idx] = 0
        shield_images[idx] += 1
        if asteroid in asteroids:
          asteroids.remove(asteroid)
