import inspect
import types


class init(type):

    def __new__(mcs, cls_name, bases, attrs):
        for k, func in attrs.items():
            if not isinstance(func, types.FunctionType):
                continue

            defaults = []
            params = inspect.signature(func).parameters
            for par_name, par_ann in func.__annotations__.items():
                param = params[par_name]
                try:
                    par_def = par_ann() if param.default is inspect.Parameter.empty else param.default
                except:
                    par_def = None
                defaults.append(par_def)
            func.__defaults__ = tuple(defaults)

        return super().__new__(mcs, cls_name, bases, attrs)
