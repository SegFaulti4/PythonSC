def moar(a, b, n):
    a_sum = sum(1 if x % n == 0 else 0 for x in a)
    b_sum = sum(1 if x % n == 0 else 0 for x in b)
    return a_sum > b_sum
