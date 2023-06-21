"""
Viva:
Menos de 2 vizinhas, morre
Mais de 3 vizinhos, morre

Morta:
3 vizinhos, vive
"""
import curses

import numpy as np

width = 238
height = 57
inicial = None
mortovivo = ' ▉'

stdscr = curses.initscr()


def randomize():
    return np.random.randint(0, 2, size=(height, width))


def show(screen):
    for i, row in enumerate(screen):
        stdscr.addstr(i, 0, ''.join([mortovivo[x] for x in row]))

    stdscr.refresh()


def tick(tela):
    somas = np.array([np.roll(y, r2, axis=1)
                      for y in np.array([np.roll(tela, r1, axis=0)
                                         for r1 in [-1, 0, 1]])
                      for r2 in [-1, 0, 1]]).sum(axis=0) - tela

    return np.bitwise_or(somas == 3,
                         np.bitwise_and(tela, somas == 2)).astype(int)


def main():
    try:
        tela = randomize()
        stdscr.clear()
        stdscr.nodelay(True)
        while True:
            show(tela)
            tela = tick(tela)
            tecla = stdscr.getch()
            if tecla != curses.ERR:
                if tecla in [ord('q'), ord('Q')]:
                    break
                tela = randomize()
    except KeyboardInterrupt:
        print('Done')


if __name__ == '__main__':
    main()
