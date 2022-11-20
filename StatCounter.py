def statcounter():
    counter = dict()
    func = yield counter

    while True:
        def decorator(fun):
            counter[fun] = 0

            def new_fun(*args, **kwargs):
                counter[fun] += 1
                return fun(*args, **kwargs)

            return new_fun

        func = yield decorator(func)


stat = statcounter()
stats = next(stat)

@stat.send
def f1(a): return a+1

@stat.send
def f2(a, b): return f1(a)+f1(b)

print(f1(f2(2,3)+f2(5,6)))
print(*((f.__name__, c) for f, c in stats.items()))