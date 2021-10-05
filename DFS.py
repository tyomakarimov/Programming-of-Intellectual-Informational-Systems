import the_matrix
from helpers import the_neighbours

def DFS(start, target):
  current_matrix = the_matrix.generate_matrix()
  stack = [start]
  path = []
  visited = []
  while len(stack) > 0:
    current = stack.pop()
    visited.append(current)
    if current == target:
      break
    neighbours = the_neighbours.get_neighbours(current_matrix, current)
    for neighbour in neighbours:
      if neighbour not in visited:
        stack.append(neighbour)
        path.append({ 'current': current, 'next': neighbour })
  path_to_target = [target]
  while target != start:
    for step in path:
      if step['next'] == target:
        target = step['current']
        path_to_target.insert(0, step['current'])
  return path_to_target
