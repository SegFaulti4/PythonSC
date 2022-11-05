import sys

x, y, z = map(float, input().split(','))
min_x, min_y, min_z = x, y, z
max_x, max_y, max_z = x, y, z

for line in sys.stdin:
    if line == "" or line == "\n":
        break
    x, y, z = map(float, line.split(','))
    min_x, min_y, min_z = min(x, min_x), min(y, min_y), min(z, min_z)
    max_x, max_y, max_z = max(x, max_x), max(y, max_y), max(z, max_z)

print((max_x - min_x) * (max_y - min_y) * (max_z - min_z))
