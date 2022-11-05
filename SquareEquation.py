from math import sqrt

a, b, c = map(float, input().split(','))

if a == 0.:
    if b == 0.:
        if c == 0.:
            print(-1)
        else:
            print(0)
    else:
        print(-c / b)
else:
    d = b * b - 4. * a * c
    if d < 0.:
        print(0)
    elif d > 0.:
        res1 = (-b - sqrt(d)) / (2. * a)
        res2 = (-b + sqrt(d)) / (2. * a)
        print(min(res1, res2), max(res1, res2))
    else:
        print(-b / (2. * a))
