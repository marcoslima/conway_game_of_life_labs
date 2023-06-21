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
inicial = np.random.randint(0, 2, size=(height, width))

stdscr = curses.initscr()


def show(screen):
    mortovivo = ' ▉'
    for i, row in enumerate(screen):
        stdscr.addstr(i, 0, ''.join([mortovivo[x] for x in row]))

    stdscr.refresh()


def tick(tela):
    """
    (roll axis=0), (roll axis=1)
    1 2 3
    4 5 6
    7 8 9
    -1, -1   -1, 0   -1, 1
     0, -1    0, 0    0, 1
     1, -1    1, 0    1, 1
    """
    r5 = tela.copy()
    r1 = np.roll(r5, -1, axis=(0, 1))
    r2 = np.roll(r5, -1, axis=0)
    r3 = np.roll(np.roll(r5, -1, axis=0), 1, axis=1)
    r4 = np.roll(r5, -1, axis=1)
    r6 = np.roll(r5, 1, axis=1)
    r7 = np.roll(np.roll(r5, 1, axis=0), -1, axis=1)
    r8 = np.roll(r5, 1, axis=0)
    r9 = np.roll(r5, 1, axis=(0, 1))
    somas = r1 + r2 + r3 + r4 + r6 + r7 + r8 + r9
    lives = somas == 2
    treses = somas == 3
    x = np.bitwise_and(r5, lives)  # Se já vivo, continua vivo
    nova_tela = np.bitwise_or(treses, x).astype(int)  # Vivo ou não, vive
    return nova_tela.copy()


def main():
    try:
        tela = inicial
        stdscr.clear()
        while True:
            show(tela)
            tela = tick(tela)
    except KeyboardInterrupt:
        print('Done')


if __name__ == '__main__':
    main()
