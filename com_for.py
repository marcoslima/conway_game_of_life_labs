"""
Viva:
Menos de 2 vizinhas, morre
Mais de 3 vizinhos, morre

Morta:
3 vizinhos, vive
"""
import copy
import curses
from time import time
from random import randint
width = 250
height = 57
inicial = [[randint(0, 1) for _ in range(width)] for _ in range(height)]

stdscr = curses.initscr()


def show(screen):
    stdscr.clear()
    mortovivo = ' ▉'
    for i, row in enumerate(screen):
        stdscr.addstr(i, 0, ''.join([mortovivo[x] for x in row]))
    stdscr.refresh()


def clamp(value, minv, maxv):
    if value < minv:
        return maxv
    if value > maxv:
        return minv
    return value


def count_vizinho(row, col, tela):
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
        y = clamp(row + off_y, 0, height-1)
        x = clamp(col + off_x, 0, width-1)
        count += tela[y][x]
    return count


def tick(tela):
    nova_tela = copy.deepcopy(tela)
    for r, row in enumerate(tela):
        for c, cell in enumerate(row):
            vizinhos = count_vizinho(r, c, tela)
            if cell == 0 and vizinhos == 3:
                nova_tela[r][c] = 1
            elif vizinhos not in [2, 3]:
                nova_tela[r][c] = 0
    return nova_tela


def main():
    count = 0
    start = time()
    try:
        tela = inicial
        while True:
            show(tela)
            tela = tick(tela)
            count += 1
    except KeyboardInterrupt:
        end = time()
        print(f'tick+render: {count / (end-start):.04f} FPS')


if __name__ == '__main__':
    main()
