filename = "test.txt"
line1 = 1
line2 = 2 

with open(filename, 'r') as f:
    lines = f.readlines()

lines[line1-1], lines[line2-1] = lines[line2-1], lines[line1-1]

with open(filename, 'w') as f:
    f.writelines(lines)