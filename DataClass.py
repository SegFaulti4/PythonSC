def sloter(fields, default):

    class slotted:
        __slots__ = list(fields)

        def __init__(self):
            for field in fields:
                self.__setattr__(field, default)

        def __delattr__(self, item):
            self.__setattr__(item, default)

        def __iter__(self):
            for field in fields:
                yield self.__getattribute__(field)

    return slotted
