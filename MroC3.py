from sys import stdin, exit
from typing import Dict, List, Optional


class Lin:
    deps: Dict[str, int]

    def __init__(self, ls: List[str]):
        self.deps = dict()
        for i, s in enumerate(ls):
            self.deps[s] = i

    def is_in_tail(self, s: str) -> bool:
        return s in self.deps and s != next(iter(self.deps))

    def del_dep(self, s: str):
        if s in self.deps:
            self.deps.pop(s)

    def get_head(self) -> str:
        return next(iter(self.deps))

    def __bool__(self):
        return bool(self.deps)


def merge(lins: List[Lin]) -> Optional[List[str]]:
    nonempty = list(filter(bool, lins))
    res = []
    while True:
        if not nonempty:
            return res

        cand = None
        for lin in nonempty:
            nothead = [l for l in nonempty if l.is_in_tail(lin.get_head())]
            if nothead:
                cand = None
            else:
                cand = lin.get_head()
                break

        if cand is None:
            return None
        res.append(cand)

        for lin in nonempty:
            lin.del_dep(cand)
        nonempty = list(filter(bool, nonempty))


def mro(classes: Dict[str, Lin], class_name: str, inherited: List[str]) -> Optional[List[str]]:
    lins = [classes[inh] for inh in inherited] + [Lin(inherited)]

    if lins:
        tail = merge(lins)
        if tail is None:
            return None
        return [class_name] + tail

    return [class_name]


if __name__ == '__main__':
    classes: Dict[str, Lin] = dict()

    for line in stdin:
        if line == "" or line == "\n":
            break

        if line.startswith('class '):
            head_start = line.find('class ') + len('class ')
            head_end = line.find(':')

            head = line[head_start:head_end].strip()
            if head.endswith(')'):
                name = head[:head.find('(')].strip()
                inherited = list(map(lambda x: x.strip(), head[head.find('(') + 1:-1].split(',')))
            else:
                name = head
                inherited = []

            ls = mro(classes, name, inherited)
            if ls is None:
                print("No")
                exit()
            else:
                classes[name] = Lin(ls)

    print("Yes")
