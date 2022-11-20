def fix(n):
    def round_if_float(x):
        if isinstance(x, float):
            return round(x, ndigits=n)
        return x

    def decorator(fun):
        def new_fun(*args, **kwargs):
            return round_if_float(
                fun(*map(round_if_float, args),
                    **{k: round_if_float(v) for k, v in kwargs.items()})
            )
        return new_fun

    return decorator
