import types
import numbers


class fixed(type):

    def __new__(mcs, cls_name, bases, attrs, ndigits=3):
        for k, func in attrs.items():
            if not isinstance(func, types.FunctionType):
                continue

            def decorator(fun):
                def new_func(*args, **kwargs):
                    res = fun(*args, **kwargs)
                    if isinstance(res, numbers.Real):
                        res = round(res, ndigits=ndigits)
                    return res
                return new_func

            attrs[k] = decorator(func)

        return super().__new__(mcs, cls_name, bases, attrs)
