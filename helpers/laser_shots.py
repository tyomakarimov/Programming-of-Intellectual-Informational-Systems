def handle_laser_shots(
  shots: list,
  aliens: list,
  shields: list,
  shield_images: list,
  coordinates: list,
  previous_paths: list,
  score: int
):
  new_score = score
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
        new_score = new_score + 10
        for idx, coord in enumerate(coordinates):
          if coord['x'] == alien.x and coord['y'] == alien.y:
            coordinates.remove(coord)
            previous_paths.pop(idx)
  return new_score 
