from random import uniform
from math import cos, sin, sqrt, acos, copysign


def randsquare(a, b):
    def dot(a, b):
        return a[0] * b[0] + a[1] * b[1]

    def length(v):
        return sqrt(dot(v, v))

    def angle(a, b):
        det = a[0] * b[1] - a[1] * b[0]
        return copysign(acos(dot(a, b) / (length(a) * length(b))), det)

    def rotate(v, ang):
        return v[0] * cos(ang) - v[1] * sin(ang), \
               v[0] * sin(ang) + v[1] * cos(ang)

    v = b[0] - a[0], b[1] - a[1]
    side = length(v) / sqrt(2.)
    ang = -angle(v, (side, side))

    x, y = uniform(0., side), uniform(0., side)
    x, y = rotate((x, y), ang)

    return a[0] + x, a[1] + y
