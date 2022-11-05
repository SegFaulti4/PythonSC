from sys import stdin
from collections import defaultdict

persons = set()
connections = defaultdict(set)

for line in stdin:
    if line == "" or line == "\n":
        break

    a, b = map(int, line.strip().split(', '))
    if a == 0 and b == 0:
        break
    persons.add(a)
    persons.add(b)
    if a != b:
        connections[a].add(b)
        connections[b].add(a)

for person in sorted(connections.keys()):
    if len(connections[person]) == len(persons) - 1:
        print(person, end=' ')
