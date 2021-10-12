def get_the_shortest_path(paths):
  the_shortest_path = list(paths[0].keys())[0]
  for path in paths:
    key = list(path.keys())[0]
    if (path[key] < the_shortest_path):
      the_shortest_path = key
  return the_shortest_path
