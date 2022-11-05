from math import log10

k = int(input())

for n in range(0, 100):
    x = (k * pow(10, n) - k * k) // (10 * k - 1)

    if ((x * 10 + k) * k == k * pow(10, n) + x) \
            and ((x == 0 and n == 0) or int(log10(x * 10)) == n):
        print(x * 10 + k)
        break
