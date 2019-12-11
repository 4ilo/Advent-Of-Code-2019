#!/usr/bin/python3

import io
from processor import processor
from collections import defaultdict
from contextlib import redirect_stdout

FILE = "input.txt"

move_x = [0, +1, 0, -1]
move_y = [-1, 0, +1, 0]

def rotate_and_move(pos, direction, turn):
    if turn == 1:
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

    pos = (pos[0] + move_x[direction], pos[1] + move_y[direction])

    return pos, direction

def paint(program, start_value):
    cpu = processor(program.copy(), 10000)

    field = defaultdict(lambda: 0)
    pos = (0, 0)
    direction = 0
    field[pos] = start_value

    stop = False
    while not stop:
        ret = 0
        f = io.StringIO()
        with redirect_stdout(f):
            data = [field[pos]]
            while ret == 0:
                ret = cpu.run(data)

            if ret == 99:
                stop = True

        outp = [int(x) for x in f.getvalue().split("\n")[:-1]]
        field[pos] = outp[0]

        pos, direction = rotate_and_move(pos, direction, outp[1])

    return len(field), field

def plot_field(field):
    maxx = max(field)[0]
    maxy = max(field, key=lambda i:i[1])[1] + 1

    for y in range(maxy):
        for x in range(maxx):
            if field[(x, y)] == 0:
                print(" ", end="")
            else:
                print("#", end="")
        print("")

if __name__ == "__main__":
    with open(FILE) as file:
        program = [int(x) for x in file.read().split(",")]
        #print(program)

    # Part 1
    result, _ = paint(program, start_value=0)
    print("Result 1: {}".format(result))

    # Part 2
    result2, field = paint(program, start_value=1)
    print("Result 2:")
    plot_field(field)

