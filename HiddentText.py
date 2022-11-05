def inspect_second_symbol_appearance(s1, s2, step):
    return s1[step::1 + step].find(s2) != -1


def inspect_first_symbol_appearance(s1, s2, offset):
    snd_sym_idx = s1.find(s2[0])
    if snd_sym_idx == -1:
        return False
    if len(s2) == 1:
        return True
    if snd_sym_idx + 1 == len(s1):
        return False

    if inspect_second_symbol_appearance(s1[snd_sym_idx + 1:], s2[1:], step=offset + snd_sym_idx):
        return True
    return inspect_first_symbol_appearance(s1[snd_sym_idx + 1:], s2, offset=snd_sym_idx + 1)


def is_hidden(s1, s2):
    fst_sym_idx = s1.find(s2[0])
    if fst_sym_idx == -1:
        return False
    if len(s2) == 1:
        return True
    if fst_sym_idx + 1 == len(s1):
        return False

    if inspect_first_symbol_appearance(s1[fst_sym_idx + 1:], s2[1:], offset=0):
        return True
    return is_hidden(s1[fst_sym_idx + 1:], s2)


if is_hidden(input().strip(), input().strip()):
    print("YES")
else:
    print("NO")
