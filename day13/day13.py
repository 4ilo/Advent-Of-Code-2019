#!/usr/bin/python3

import io
from collections import defaultdict
from processor import processor
from contextlib import redirect_stdout

def render_field(data):
    field = defaultdict(lambda: 0)
    for tile in data:
        if tile[0] == -1 and tile[1] == 0:
            print("score: {}".format(tile[2]))
        else:
            field.update({(tile[0], tile[1]): tile[2]})

    print(field)
    maxx = max(field)[0] + 1
    maxy = max(field, key=lambda i:i[1])[1] + 1
    print(maxx, maxy)

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

if __name__ == "__main__":
    with open("input.txt") as file:
        program = [int(x) for x in file.read().split(",")]
        #print(program)

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
    ret = 0
    program[0] = 2
    cpu = processor(program, 10000)
    while True:
        data = []
        f = io.StringIO()
        with redirect_stdout(f):
            while ret == 0:
                ret = cpu.run(data)

        data = [int(x) for x in f.getvalue().split("\n")[:-1]]
        data = [data[i:i+3] for i in range(0, len(data), 3)]
        render_field(data)
        #print(data)

        if ret == -1:
            data = [int(input("Joystick: "))]

    print(ret)
