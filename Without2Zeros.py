def No_2Zero(N, K):
    if N == 0:
        return 0
    count_non_zero, count_zero = 1, 1
    for _ in range(N - 1):
        count_non_zero, count_zero = (K - 1) * count_non_zero + count_zero, (K - 1) * count_non_zero
    return (K - 1) * count_non_zero
