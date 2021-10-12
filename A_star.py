from queue import PriorityQueue

import the_matrix
from helpers import the_neighbours

def heuristic(element1, element2):
  x1, y1 = the_neighbours.get_element_indeces(element1)
  x2, y2 = the_neighbours.get_element_indeces(element2)
  return abs(x1 - x2) + abs(y1 - y2)

def A_star(start, target):
  current_matrix = the_matrix.generate_matrix()
  count = 0
  queue = PriorityQueue()
  queue.put((0, count, start))
  g_score = { i: float('inf') for i in range(1, 401)  }
  g_score[start] = 0
  f_score = { i: float('inf') for i in range(1, 401) }
  f_score[start] = heuristic(start, target)
  queue_elements = { start }
  path = []
  while not queue.empty():
    current = queue.get()[2]
    queue_elements.remove(current)
    if current == target:
      break
    neighbours = the_neighbours.get_neighbours(current_matrix, current)
    for neighbour in neighbours:
      temp_g_score = g_score[current] + 1
      if temp_g_score < g_score[neighbour]:
        g_score[neighbour] = temp_g_score
        f_score[neighbour] = temp_g_score + heuristic(neighbour, target)
        if neighbour not in queue_elements:
          count += 1
          queue.put((f_score[neighbour], count, neighbour))
          queue_elements.add(neighbour)
          path.append({ 'current': current, 'next': neighbour })
  path_to_target = [target]
  while target != start:
    for step in path:
      if step['next'] == target:
        target = step['current']
        path_to_target.insert(0, step['current'])
  return path_to_target

print(A_star(86, 377))
