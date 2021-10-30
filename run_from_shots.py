import aliens

def run_from_shots(shots: list, the_aliens: list, shields: list):
  xs = []
  shots_xs = []
  shields_xs = []
  the_lowest = [0]
  for an_alien in the_aliens:
    if an_alien['y'] > the_lowest[0]:
      the_lowest[0] = an_alien['y']
  for an_alien in the_aliens:
    if an_alien['type'] == 'search' and an_alien['y'] == the_lowest[0]:
      xs.append(an_alien['x'] // 30)
  for shot in shots:
    x = (shot.x - 15) // 30
    shots_xs.append(x)
  for shield in shields:
    if not isinstance(shield, int):
      x = shield.x // 30
      shields_xs.append(x)
  for shot_x in shots_xs:
    if shot_x in xs and shot_x not in shields_xs:
      for idx, alien_coord in enumerate(the_aliens):
        if alien_coord['x'] // 30 == shot_x and alien_coord['type'] == 'search':
          moved = [False]
          if (alien_coord['x'] - 30) // 30 not in xs and not alien_coord['x'] // 30 == 0:
            alien_coord['x'] -= 30
            aliens.aliens[idx].x -= 30
            moved[0] = True
          if (alien_coord['x'] + 30) // 30 not in xs and not moved[0] and alien_coord['x'] // 30 == 19:
            alien_coord['x'] += 30
            aliens.aliens[idx].x += 30
            moved[0] = True
          if not moved[0] and alien_coord['x'] // 30 == 19:
            alien_coord['x'] -= 30
            aliens.aliens[idx].x -= 30
          if not moved[0] and alien_coord['x'] // 30 == 0:
            alien_coord['x'] += 30
            aliens.aliens[idx].x += 30
