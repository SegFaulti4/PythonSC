import asyncio
from typing import Callable


class FilterQueue(asyncio.Queue):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def window(self):
        if self.empty():
            return None
        return self._queue[0]

    def later(self):
        # if self.empty():
        #     raise asyncio.QueueEmpty
        # self._put(self._get())
        
        self.put_nowait(self.get_nowait())

    def __contains__(self, predicate):
        for _ in filter(predicate, self._queue):
            return True
        return False

    def get(self, predicate: Callable = None):
        if predicate is not None and predicate in self:
            while not predicate(self.window):
                self.later()

        return super().get()
