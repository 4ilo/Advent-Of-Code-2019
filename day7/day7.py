#!/usr/bin/python3

import io
import itertools
from processor import processor
from contextlib import redirect_stdout

FILE = "example.txt"
FILE = "input.txt"


def calculate_out(program, setting):
    amp_input = 0
    for thruster in setting:
        f = io.StringIO()
        cpu = processor(program.copy())

        with redirect_stdout(f):
            data = [thruster, amp_input]
            while cpu.run(data) == 0:
                pass

        amp_input = int(f.getvalue())

    return amp_input


def init_amps(amps, setting):
    for i, thruster in enumerate(setting):
        data = [thruster]
        while amps[i].run(data) == 0:
            pass


def calculate_loop(program, setting):
    amps = [processor(program.copy()) for x in setting]
    init_amps(amps, setting)

    amp_input = 0
    stop = False
    while not stop:
        for i, thruster in enumerate(setting):
            ret = 0
            f = io.StringIO()
            with redirect_stdout(f):
                data = [amp_input]
                while ret == 0:
                    ret = amps[i].run(data)

            # Store output as next input
            amp_input = int(f.getvalue())

            if ret == 99:
                stop = True

    return amp_input


if __name__ == "__main__":
    with open(FILE) as file:
        program = [int(x) for x in file.read()[:-1].split(",")]
        print(program)

    solutions = []
    for setting in itertools.permutations([0, 1, 2, 3, 4]):
        out = calculate_out(program, setting)
        solutions.append(out)
    print("Solution 1: {}".format(max(solutions)))

    solutions = []
    for setting in itertools.permutations([5, 6, 7, 8, 9]):
        out = calculate_loop(program, setting)
        solutions.append(out)
    print("Solution 2: {}".format(max(solutions)))
