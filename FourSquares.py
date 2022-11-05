from math import sqrt, floor


def generate_squares(num_of_squares, n, max_x):
    if n < 0:
        return []

    if num_of_squares == 1:
        sqr = round(sqrt(n))
        if sqr * sqr == n and sqr <= max_x:
            return [[sqr]]
        return []

    res = []
    for x in range(round(sqrt(n // 4)), max_x + 1):
        rec = generate_squares(num_of_squares - 1, n - x * x, x)
        if rec:
            res.extend([x] + rec_l for rec_l in rec)
    return res


N = int(input())
squares = generate_squares(num_of_squares=4, n=N, max_x=round(sqrt(N)) + 1)
for square in squares:
    print(" ".join(map(str, square)))
