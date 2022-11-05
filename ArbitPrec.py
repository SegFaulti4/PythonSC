import re
import decimal


def decimalize(s: str):
    return re.sub(r'(\d+(\.\d*)?)|(\.\d+)', r'decimal.Decimal(\1)', s)


def calc(expr, x):
    return eval(expr)


def solve(expr: str, prec: int):
    decimal.getcontext().prec = prec + 2

    a = decimal.Decimal("-1.5")
    b = decimal.Decimal("1.5")
    x = (a + b) / 2
    prev_x = a

    val_a, val_b = calc(expr, a), calc(expr, b)
    val_x = calc(expr, x)

    while val_a * val_x < 0 or val_x * val_b < 0:
        prev_x = x
        if val_a * val_x < 0:
            b, val_b = x, val_x
        elif val_x * val_b < 0:
            a, val_a = x, val_x
        x = (b + a) / 2
        val_x = calc(expr, x)

        if prev_x == x:
            break

    if x == 0:
        print("0." + "0" * prec)
    else:
        print(x.quantize(decimal.Decimal(10) ** -prec))


if __name__ == "__main__":
    line = input()
    expr = decimalize(line)
    prec = int(input())
    solve(expr, prec)
