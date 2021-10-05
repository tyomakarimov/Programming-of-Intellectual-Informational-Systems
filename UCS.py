from queue import PriorityQueue

import matrix
from helpers import the_neighbours

def UCS(start, target):
  current_matrix = matrix.generate_matrix()
  queue = PriorityQueue()
  queue.put((0, start))
  visited = []
  path = []
  costs = []
  elements = [start]
  while not queue.empty():
    cost, current = queue.get()
    visited.append(current)
    elements.remove(current)
    if current == target:
      break
    neighbours = the_neighbours.get_neighbours(current_matrix, current)
    for neighbour in neighbours:
      if neighbour not in visited and neighbour not in elements:
        queue.put((cost + 1, neighbour))
        costs.append(cost)
        elements.append(neighbour)
        path.append({ 'current': current, 'next': neighbour })
  path_to_target = [target]
  while target != start:
    for step in path:
      if step['next'] == target:
        target = step['current']
        path_to_target.insert(0, step['current'])
  return path_to_target
