from sys import stdin


def leader_key(leader):
    name = leader[0]
    surname = leader[1]
    team = leader[2]
    tmp = leader[3].split(':')
    time = int(tmp[0]) * 3600 + int(tmp[1]) * 60 + int(tmp[2])

    return time, surname, name, team


def print_leader(leader, col_width):
    print(
        " ".join(
            leader[i] + " " * (col_width[i] - len(leader[i])) for i in range(4)
        )
    )


leaders = []
for line in stdin:
    if line == "" or line == "\n":
        break

    leader = tuple(map(lambda x: x.strip(), line.split(' ')))
    name = leader[0]
    surname = leader[1]
    team = " ".join(leader[2:-1])
    time = leader[-1]

    leaders.append((name, surname, team, time))


leaders.sort(key=leader_key)
col_width = [max(len(leader[i]) for leader in leaders) for i in range(4) ]
placement = 1
prev_time = leaders[0][3]
print_leader(leaders[0], col_width)

for leader in leaders[1:]:
    if prev_time != leader[3]:
        placement += 1
        prev_time = leader[3]

    if placement > 3:
        break

    print_leader(leader, col_width)
