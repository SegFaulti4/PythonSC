import sys

matrix = []

for line in sys.stdin:
    if line == "" or line == "\n":
        break
    matrix.append([int(x) for x in line.strip().split(',')])

for i in range(len(matrix)):
    print(','.join(str(x) for x in matrix[i][:i + 1]), end='')
    if i > 0:
        print(',' + ','.join(str(matrix[j][i]) for j in range(i - 1, -1, -1)), end='')
    print()
