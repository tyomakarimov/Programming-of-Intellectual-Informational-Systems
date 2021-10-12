def get_the_shortest_path(paths):
  the_shortest_path = list(paths[0].keys())[0]
  index = 0
  for idx, path in enumerate(paths):
    key = list(path.keys())[0]
    if (path[key] < the_shortest_path):
      the_shortest_path = key
      index = idx
  return the_shortest_path, index
