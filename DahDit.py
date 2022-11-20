class morse:
    dot: str
    last_dot: str
    dash: str
    sig_sep: str
    char_sep: str
    end: str

    def __init__(self, s: str = None):
        self.message_chars = []
        self.char_signals = []

        if s is None:
            s = "di dit dah"

        if " " in s:
            params = list(s.split(' '))
            self.sig_sep = ' '
            self.char_sep = ', '
            self.end = '.'
        else:
            params = list(s)
            self.sig_sep = ''
            self.char_sep = ' '
            self.end = ''

        if len(params) == 2:
            self.dot, self.dash = params
            self.last_dot = self.dot
        elif len(params) == 3:
            self.dot, self.last_dot, self.dash = params
        elif len(params) == 4:
            self.dot, self.last_dot, self.dash, self.end = params

    def _char_end(self):
        if self.char_signals:
            if self.char_signals[0] == self.dot:
                self.char_signals[0] = self.last_dot
        self.message_chars.append(list(self.char_signals[::-1]))
        self.char_signals = []

    def __pos__(self):
        self.char_signals.append(self.dot)
        return self

    def __neg__(self):
        self.char_signals.append(self.dash)
        return self

    def __invert__(self):
        self._char_end()
        return self

    def __repr__(self):
        self._char_end()
        return self.char_sep.join(self.sig_sep.join(ch) for ch in self.message_chars[::-1]) + self.end
