from sys import stdin
import re


def calc(locs: dict, val: str):
    if not re.fullmatch(r'[_0-9\w+\-*/%()]*', val) or \
            re.search(r'(^|[+\-*%=(/])\d+I_LOVE_KRYJOVNIK_[a-zA-Z_]', val) or \
            re.search(r'[a-zA-Z_]+\(', val) or \
            '//' in val or '**' in val:
        # print(f"|{val}|")
        raise SyntaxError

    val = val.replace("/", "//")
    identifiers = re.findall(r'[a-zA-Z_][a-zA-Z_0-9]*', val)
    for i in identifiers:
        if i not in locs:
            raise NameError

    return eval(val, locs, {})


if __name__ == "__main__":
    ASSIGNMENT_ERR = "Assignment error"
    SYNTAX_ERR = "Syntax error"
    NAME_ERR = "Name error"
    RUNTIME_ERR = "Runtime error"

    locs = dict()

    for line in stdin:
        line = line.replace(" ", "").strip()
        line = re.sub(r'([a-zA-Z_]+)', r'I_LOVE_KRYJOVNIK_\1', line)
        if line == "":
            break

        if line.startswith('#'):
            continue

        if '=' in line:
            name = line[:line.find('=')]
            value = line[line.find('=') + 1:]

            if not name.isidentifier():
                print(ASSIGNMENT_ERR)
                continue

            assign = True
        else:
            value = line
            assign = False

        try:
            calculated = calc(locs, value)
            if not isinstance(calculated, int):
                # print(f"|{calculated}|")
                print(SYNTAX_ERR)
                continue
        except SyntaxError:
            print(SYNTAX_ERR)
            continue
        except NameError:
            print(NAME_ERR)
            continue
        except:
            print(RUNTIME_ERR)
            continue

        if assign:
            locs[name] = calculated
        else:
            print(calculated)
