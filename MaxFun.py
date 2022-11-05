def maxfun(s, *funcs):
    sums = [sum(f(x) for x in s) for f in funcs]
    max_idx, max_sum = 0, sums[0]
    for idx, func_sum in enumerate(sums):
        if func_sum >= max_sum:
            max_sum = func_sum
            max_idx = idx
    return funcs[max_idx]
