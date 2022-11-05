def callable_wrapper(f, x):
    if callable(f):
        return f(x)
    return f


def ADD(f, g):
    return lambda x: callable_wrapper(f, x) + callable_wrapper(g, x)


def SUB(f, g):
    return lambda x: callable_wrapper(f, x) - callable_wrapper(g, x)


def MUL(f, g):
    return lambda x: callable_wrapper(f, x) * callable_wrapper(g, x)


def DIV(f, g):
    return lambda x: callable_wrapper(f, x) / callable_wrapper(g, x)
