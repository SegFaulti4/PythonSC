import sys


def dots_from_left(line):
    res = 0
    for c in line:
        if c != '.':
            break
        res += 1
    return res


def dot_lines_from_top(matrix):
    res = 0
    for line in matrix:
        if not all(c == '.' for c in line):
            break
        res += 1
    return res


if __name__ == "__main__":
    rects = []
    min_x, min_y, max_x, max_y = None, None, None, None

    for line in sys.stdin:
        if line == "" or line == "\n":
            break
        s = line.split(" ")
        x, y, l, w, sym = int(s[0]), int(s[1]), int(s[2]), int(s[3]), s[4].strip()

        cur_min_x = min(x, x + l)
        cur_min_y = min(y, y + w)
        cur_max_x = max(x, x + l)
        cur_max_y = max(y, y + w)

        rects.append((cur_min_x, cur_min_y, cur_max_x, cur_max_y, sym))

        min_x = cur_min_x if min_x is None else min(cur_min_x, min_x)
        min_y = cur_min_y if min_y is None else min(cur_min_y, min_y)
        max_x = cur_max_x if max_x is None else max(cur_max_x, max_x)
        max_y = cur_max_y if max_y is None else max(cur_max_y, max_y)

    matrix = [["." for _ in range(min_x, max_x)] for __ in range(min_y, max_y)]

    for rect in rects:
        for y in range(rect[1], rect[3]):
            for x in range(rect[0], rect[2]):
                matrix[y - min_y][x - min_x] = rect[4]

    left_padding = min(dots_from_left(line) for line in matrix)
    right_padding = (max_x - min_x) - min(dots_from_left(line[::-1]) for line in matrix)

    top_padding = dot_lines_from_top(matrix)
    bottom_padding = (max_y - min_y) - dot_lines_from_top(matrix[::-1])

    for line in matrix[top_padding:bottom_padding]:
        print("".join(line[left_padding:right_padding]))
