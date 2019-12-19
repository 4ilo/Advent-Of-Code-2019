#!/usr/bin/python3

import io
from processor import processor
from contextlib import redirect_stdout

def is_affected(point, program):
    cpu = processor(program.copy(), 1000)

    f = io.StringIO()
    ret = 0
    inp = list(point)
    with redirect_stdout(f):
        while ret == 0:
            ret = cpu.run(inp)

    if ret == 99:
        return int(f.getvalue())

    return 0

if __name__ == "__main__":
    with open("input.txt") as file:
        program = [int(x) for x in file.read().split(",")]
        #print(program)

        beam = {}
        LEN = 50
        for y in range(LEN):
            for x in range(LEN):
                if is_affected((x, y), program):
                    beam[(x, y)] = True

        print("Result 1: {}". format(len(beam)))
