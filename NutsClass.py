class Nuts:
    def __init__(self, *args, **kwargs): pass
    def __getitem__(self, item): return item
    def __setitem__(self, key, value): pass
    def __delitem__(self, key): pass
    def __getattr__(self, name): return name
    def __setattr__(self, key, value): pass
    def __delattr__(self, item): pass
    def __iter__(self): return "Nuts".__iter__()
    def __repr__(self): return "Nuts"
