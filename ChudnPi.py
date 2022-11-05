import decimal


def PiGen():
    decimal.getcontext().prec = 10000

    s = decimal.Decimal(0)
    k = 0

    weird_den_const = decimal.Decimal(640320) * decimal.Decimal(640320) * decimal.Decimal(640320)
    weird_num_bias = decimal.Decimal(13591409)
    weird_num_factor = decimal.Decimal(545140134)

    factor = weird_den_const
    factor = factor.sqrt()
    factor = decimal.Decimal(12) / factor

    while True:
        weird_num = weird_num_factor * decimal.Decimal(k) + weird_num_bias
        s += factor * weird_num
        yield decimal.Decimal(1) / s

        k += 1
        factor *= decimal.Decimal(-1)
        for i in range(6):
            factor *= decimal.Decimal(6 * k - i)
        for i in range(3):
            factor /= decimal.Decimal(3 * k - i)
        factor /= decimal.Decimal(k) * decimal.Decimal(k) * decimal.Decimal(k)
        factor /= weird_den_const
