class NegExt:

    def __neg__(self):
        if hasattr(super(), "__neg__") and callable(getattr(super(), "__neg__")):
            res = super().__neg__()
        else:
            try:
                res = self[1:-1]
            except:
                res = self
        return self.__class__(res)
