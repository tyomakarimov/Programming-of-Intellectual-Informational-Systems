from helpers import the_neighbours
import aliens

def run_from_shots(shots: list, the_aliens: list, shields: list, move_left: bool):
  aliens_xs = []
  new_aliens_xs_left = []
  new_aliens_xs_right = []
  shots_xs = []
  shields_xs = []
  for alien in the_aliens:
    x = the_neighbours.get_element_indeces(alien)[1]
    aliens_xs.append(x)
  for shot in shots:
    x = (shot.x - 15) // 30
    shots_xs.append(x)
  for shield in shields:
    if not isinstance(shield, int):
      x = shield.x // 30
      shields_xs.append(x)
  for coords in aliens.alien_coordinates:
    new_aliens_xs_left.append((coords['x'] - 30) // 30)
    new_aliens_xs_right.append((coords['x'] + 30) // 30)
  for shot_x in shots_xs:
    if shot_x in aliens_xs and shot_x not in shields_xs:
      left = list(filter(lambda x: x < 0, new_aliens_xs_left))
      right = list(filter(lambda x: x > 19, new_aliens_xs_right))
      for coords in aliens.alien_coordinates:
        if len(left) == 0 and move_left:
          coords['x'] -= 30
          for value in new_aliens_xs_left:
            value -= 1
          left = list(filter(lambda x: x < 0, new_aliens_xs_left))
        else:
          coords['x'] += 30
          for value in new_aliens_xs_right:
            value += 1
          right = list(filter(lambda x: x > 19, new_aliens_xs_right))
        if len(right) == 0 and not move_left:
          coords['x'] += 30
        else:
          coords['x'] -= 30
      for an_alien in aliens.aliens:
        if len(left) == 0 and move_left:
          an_alien.x -= 30
        elif len(right) == 0 and not move_left:
          an_alien.x += 30
