import curses

from basic_conway_ui_adapter import BasicUiConwayAdapter


class CursesUiConwayAdapter(BasicUiConwayAdapter):
    def update_screen(self, data):
        mortovivo = ' ▉'
        for i, row in enumerate(data):
            self.stdscr.addstr(i, 0, ''.join([mortovivo[x] for x in row]))

        self.stdscr.refresh()

    def __init__(self):
        super().__init__()
        self.stdscr = curses.initscr()
