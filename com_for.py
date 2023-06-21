"""
Viva:
Menos de 2 vizinhas, morre
Mais de 3 vizinhos, morre

Morta:
3 vizinhos, vive
"""
import copy
from random import randint

from basic_conway import BasicConway
from basic_conway_ui_adapter import UiConwayPort
from curses_ui_conway import CursesUiConwayAdapter


class PurePyConway(BasicConway, UiConwayPort):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = self._make_initial_state()

    def show(self):
        self.update_screen(self.data)

    def tick(self):
        nova_tela = copy.deepcopy(self.data)
        for r, row in enumerate(self.data):
            for c, cell in enumerate(row):
                vizinhos = self._count_vizinho(r, c, self.data)
                if cell == 0 and vizinhos == 3:
                    nova_tela[r][c] = 1
                elif vizinhos not in [2, 3]:
                    nova_tela[r][c] = 0
        self.data = nova_tela

    def _make_initial_state(self):
        return [[randint(0, 1)
                 for _ in range(self.width)]
                for _ in range(self.height)]

    @staticmethod
    def _clamp(value, minv, maxv):
        if value < minv:
            return maxv
        if value > maxv:
            return minv
        return value

    def _count_vizinho(self, row, col, tela):
        """
            123
            456
            789
        """
        vizinhos = ((-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 1),
                    (1, -1), (1, 0), (1, 1)
                    )
        count = 0
        for off_y, off_x in vizinhos:
            y = self._clamp(row + off_y, 0, self.height-1)
            x = self._clamp(col + off_x, 0, self.width-1)
            count += tela[y][x]
        return count


if __name__ == '__main__':
    ui_adapter = CursesUiConwayAdapter()
    app = PurePyConway(238, 57)
    app.set_ui_adapter(ui_adapter)
    app.run()
