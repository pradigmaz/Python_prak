import csv

with open('дз/github/data2.csv', newline='') as f:
    reader = csv.reader(f)
    data = [row for row in reader]

for row in data:
    print(row)

