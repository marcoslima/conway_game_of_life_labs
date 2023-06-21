from abc import ABC, abstractmethod
from time import time


class BasicConway(ABC):
    def __init__(self, width=80, height=25):
        self.width = width
        self.height = height

    @abstractmethod
    def show(self):
        raise NotImplementedError

    @abstractmethod
    def tick(self):
        raise NotImplementedError

    @abstractmethod
    def _make_initial_state(self):
        raise NotImplementedError

    def run(self):
        count = 0
        start = time()
        try:
            while True:
                self.show()
                self.tick()
                count += 1

        except KeyboardInterrupt:
            end = time()
            print(f'tick+render: {count / (end - start):.04f} FPS')
