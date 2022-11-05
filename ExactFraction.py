import fractions
import re


def replace_func(match_obj: re.Match):
    s = match_obj.group(0)
    if '.' in s:
        pos = s.find('.')
        pr = len(s) - 1 - pos

        num = s[:pos] + s[pos + 1:]
        den = "1" + "0" * pr

        while num != "0":
            if num[0] != "0":
                break
            num = num[1:]

        res = "(fractions.Fraction(" + num + ")"
        res += "/fractions.Fraction(" + den + "))"
        return res
    return "fractions.Fraction(" + s + ")"


def fractionate(s: str):
    return re.sub(r'(\d+(\.\d*)?)|(\.\d+)', replace_func, s)


if __name__ == "__main__":
    op = input().strip()
    replaced = fractionate(op)
    print(eval(replaced))
