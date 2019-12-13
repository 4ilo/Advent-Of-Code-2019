#!/usr/bin/python3

import io
from collections import defaultdict
from processor import processor
from contextlib import redirect_stdout

field = defaultdict(lambda: 0)

INTERACTIVE = False


def render_field(data):
    for tile in data:
        if tile[0] == -1 and tile[1] == 0:
            score = tile[2]
            print("score: {}".format(score))
        else:
            field.update({(tile[0], tile[1]): tile[2]})

    maxx = max(field)[0] + 1
    maxy = max(field, key=lambda i:i[1])[1] + 1

    for y in range(maxy):
        for x in range(maxx):
            tile = field[(x, y)]
            if tile == 0:
                print(" ", end="")
            if tile == 1:
                print("|", end="")
            if tile == 2:
                print("#", end="")
            if tile == 3:
                print("-", end="")
            if tile == 4:
                print("o", end="")

        print("")


def get_result(data):
    for tile in data:
        if tile[0] == -1 and tile[1] == 0:
            return tile[2]


if __name__ == "__main__":
    with open("input.txt") as file:
        program = [int(x) for x in file.read().split(",")]
        # print(program)

    # Part 1
    ret = 0
    cpu = processor(program.copy(), 10000)
    f = io.StringIO()
    with redirect_stdout(f):
        while ret == 0:
            ret = cpu.run([])

    data = [int(x) for x in f.getvalue().split("\n")[:-1]]
    data = [data[i:i+3] for i in range(0, len(data), 3)]
    blocks = list(filter(lambda x: x[2] == 2, data))
    print("Result 1: {}".format(len(blocks)))

    # Part 2
    program[0] = 2
    if not INTERACTIVE:
        program[1744:1744 + 46] = [3] * 46          # Change puzzle input with a solid wall at the bottom of the field

    cpu = processor(program, 10000)
    inp = []
    while True:
        f = io.StringIO()
        ret = 0
        with redirect_stdout(f):
            while ret == 0:
                ret = cpu.run(inp)

        data = [int(x) for x in f.getvalue().split("\n")[:-1]]
        data = [data[i:i+3] for i in range(0, len(data), 3)]
        if INTERACTIVE:
            render_field(data)

        if ret == -1:
            if INTERACTIVE:
                inp = [int(input("Joystick: "))]
            else:
                inp = [0]

        if ret == 99:
            print("Result 2: {}".format(get_result(data)))
            exit()
