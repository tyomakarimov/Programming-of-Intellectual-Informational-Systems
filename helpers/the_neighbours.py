def get_element_indeces(element: int):
  remaining = element % 20
  indeces = []
  if (remaining == 0):
    indeces.append(int(element / 20 - 1))
    indeces.append(19)
  else:
    indeces.append(int((element - remaining) / 20))
    indeces.append(remaining - 1)
  return indeces

def get_element(x: int, y: int):
  return x * 20 + y + 1

def get_neighbours(matrix: list, element: int):
  neighbours = []
  candidates = []
  if element % 20 == 0:
    candidates.append(element - 1)
    if element != 400:
      candidates.append(element + 20)
  elif element % 20 == 1:
    candidates.append(element + 1)
    if element != 381:
      candidates.append(element + 20)
  elif element < 20 and element != 1:
    candidates.append(element - 1)
    candidates.append(element + 1)
    candidates.append(element + 20)
  elif element > 381 and element != 400:
    candidates.append(element - 1)
    candidates.append(element + 1)
  else:
    candidates.append(element - 1)
    candidates.append(element + 1)
    candidates.append(element + 20)

  for value in candidates:
    indeces = get_element_indeces(value)
    if matrix[indeces[0]][indeces[1]] == 0 or matrix[indeces[0]][indeces[1]] == 3 and value > 100:
      neighbours.append(value)
  return sorted(neighbours, key=int, reverse=True)
