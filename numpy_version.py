"""
Viva:
Menos de 2 vizinhas, morre
Mais de 3 vizinhos, morre

Morta:
3 vizinhos, vive
"""

import numpy as np

from basic_conway import BasicConway
from curses_ui_conway import CursesUiConwayAdapter
from basic_conway_ui_adapter import UiConwayPort


class NumpyConway(BasicConway, UiConwayPort):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = self._make_initial_state()

    def show(self):
        self.update_screen(self.data)

    def tick(self):
        somas = np.array([np.roll(y, r2, axis=1)
                          for y in np.array([np.roll(self.data, r1, axis=0)
                                             for r1 in [-1, 0, 1]])
                          for r2 in [-1, 0, 1]]).sum(axis=0) - self.data

        self.data = np.bitwise_or(somas == 3,
                                  np.bitwise_and(self.data,
                                                 somas == 2)).astype(np.uint8)

    def _make_initial_state(self):
        return np.random.randint(0, 2, size=(self.height, self.width),
                                 dtype=np.uint8)


if __name__ == '__main__':
    ui_adapter = CursesUiConwayAdapter()
    app = NumpyConway(238, 57)
    app.set_ui_adapter(ui_adapter)
    app.run()
