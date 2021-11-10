import csv  

header = ['win', 'time', 'score', 'player_health', 'algorithm']

# with open('output.csv', 'a', encoding='UTF8', newline='') as f:
#   writer = csv.writer(f)
#   writer.writerow(header)

def write_to_scv(data):
  with open('output.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)

def write_result(input, output):
  header = ['score', 'time']
  with open('output2.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(input)):
      row = []
      row.append(input[i][0])
      row.append(output[i])
      writer.writerow(row)
