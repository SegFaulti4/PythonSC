from collections import defaultdict
from copy import deepcopy


class Spiral:

    def __init__(self, s: str):
        self.groups = defaultdict(int)
        self.seq = list()

        for ch in s:
            if ch not in self.groups:
                self.seq.append(ch)
            self.groups[ch] += 1

    def __add__(self, other):
        if not isinstance(other, Spiral):
            return NotImplemented

        new_sp = deepcopy(self)
        for ch in other.seq:
            if ch not in new_sp.groups:
                new_sp.seq.append(ch)
            new_sp.groups[ch] += other.groups[ch]

        return new_sp

    def __sub__(self, other):
        if not isinstance(other, Spiral):
            return NotImplemented

        new_sp = deepcopy(self)
        new_seq = []
        for ch in new_sp.seq:
            if ch in other.groups:
                new_sp.groups[ch] = max(0, new_sp.groups[ch] - other.groups[ch])
            if new_sp.groups[ch] == 0:
                del new_sp.groups[ch]
            else:
                new_seq.append(ch)

        new_sp.seq = new_seq
        return new_sp

    def __mul__(self, other):
        if not isinstance(other, int) or other < 1:
            return NotImplemented

        new_sp = deepcopy(self)
        for ch in new_sp.groups:
            new_sp.groups[ch] *= other

        return new_sp

    def __iter__(self):
        for ch in self.seq:
            for _ in range(self.groups[ch]):
                yield ch

    def __repr__(self):
        length = sum(self.groups.values()) - 1

        rotation_map = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0)
        }

        x, y = 0, 0
        min_x, max_x = x, x
        min_y, max_y = y, y
        dx, dy = 1, 0
        arc_len = 1

        while length:
            step = min(length, arc_len)
            x += step * dx
            y += step * dy

            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)

            dx, dy = rotation_map[(dx, dy)]
            arc_len += 1
            length -= step

        n_rows = max_x - min_x + 1
        n_cols = max_y - min_y + 1

        matrix = [[" " for _ in range(n_rows)] for __ in range(n_cols)]
        # matrix[y][x]

        x, y = -min_x, -min_y
        dx, dy = 1, 0
        arc_len = 1
        step = arc_len

        for ch in self:
            matrix[y][x] = ch
            x += dx
            y += dy
            step -= 1

            if not step:
                dx, dy = rotation_map[(dx, dy)]
                arc_len += 1
                step = arc_len

        return '\n'.join(''.join(col) for col in matrix)
