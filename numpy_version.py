"""
Viva:
Menos de 2 vizinhas, morre
Mais de 3 vizinhos, morre

Morta:
3 vizinhos, vive
"""
import curses

import numpy as np

from basic_conway import BasicConway


class NumpyConway(BasicConway):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.stdscr = curses.initscr()
        self.screen = self._make_initial_state()

    def show(self):
        mortovivo = ' ▉'
        for i, row in enumerate(self.screen):
            self.stdscr.addstr(i, 0, ''.join([mortovivo[x] for x in row]))

        self.stdscr.refresh()

    def tick(self):
        somas = np.array([np.roll(y, r2, axis=1)
                          for y in np.array([np.roll(self.screen, r1, axis=0)
                                             for r1 in [-1, 0, 1]])
                          for r2 in [-1, 0, 1]]).sum(axis=0) - self.screen

        self.screen = np.bitwise_or(somas == 3,
                                    np.bitwise_and(self.screen,
                                                   somas == 2)).astype(int)

    def _make_initial_state(self):
        return np.random.randint(0, 2, size=(self.height, self.width))


if __name__ == '__main__':
    app = NumpyConway(238, 57)
    app.run()
