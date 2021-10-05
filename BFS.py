import the_matrix
from helpers import the_neighbours

def BFS(start, target):
  current_matrix = the_matrix.generate_matrix()
  queue = [start]
  path = []
  visited = []
  while len(queue) > 0:
    current = queue[0]
    queue.remove(queue[0])
    visited.append(current)
    if current == target:
      break
    else:
      neighbours = the_neighbours.get_neighbours(current_matrix, current)
      for neighbour in neighbours:
        if neighbour not in visited and neighbour not in queue:
          queue.append(neighbour)
          path.append({ 'current': current, 'next': neighbour })
  path_to_target = [target]
  while target != start:
    for step in path:
      if step['next'] == target:
        target = step['current']
        path_to_target.insert(0, step['current'])
  return path_to_target
