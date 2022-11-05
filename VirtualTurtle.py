def turtle(coord, dr):
    dir_map = {
        0: (1, 0),
        1: (0, 1),
        2: (-1, 0),
        3: (0, -1)
    }

    while True:
        comm = yield coord
        if comm == 'f':
            coord = coord[0] + dir_map[dr][0], coord[1] + dir_map[dr][1]
        elif comm == 'l':
            dr = (dr + 1) % 4
        elif comm == 'r':
            dr = (dr + 3) % 4
