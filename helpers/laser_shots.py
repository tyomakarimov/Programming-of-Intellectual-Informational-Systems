def handle_laser_shots(shots: list, aliens: list, shields: list, shield_images: list):
  for shot in shots:
    shot.y -= 7
    for idx, shield in enumerate(shields):
      if shield != 0 and (shield.colliderect(shot)):
        if shield_images[idx] == 5:
          shields[idx] = 0
        shield_images[idx] += 1
        if shot in shots:
          shots.remove(shot)
    for alien in aliens:
      if (alien.colliderect(shot)):
        if shot in shots:
          shots.remove(shot)
        aliens.remove(alien)
