class Pushpull:
    pos = 0

    def __init__(self, n=0):
        Pushpull.pos = n

    def __repr__(self):
        if Pushpull.pos < 0:
            return f"<{-Pushpull.pos}<"
        elif Pushpull.pos > 0:
            return f">{Pushpull.pos}>"
        return "<0>"

    def __iter__(self):
        for x in range(0, Pushpull.pos, -1 if Pushpull.pos < 0 else 1):
            yield x

    @staticmethod
    def push(n=1):
        Pushpull.pos += n

    @staticmethod
    def pull(n=1):
        Pushpull.pos -= n
