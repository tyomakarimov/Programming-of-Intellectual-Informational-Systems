import csv  

header = ['win', 'time', 'score', 'player_health', 'algorithm']

# with open('output.csv', 'a', encoding='UTF8', newline='') as f:
#   writer = csv.writer(f)
#   writer.writerow(header)

def write_to_scv(data):
  with open('output.csv', 'a', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data)
