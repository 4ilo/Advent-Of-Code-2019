#!/usr/bin/python3

from processor import processor
import io
import sys
from contextlib import redirect_stdout
import itertools

FILE = "example.txt"
#FILE = "input.txt"

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
        while amps[i].run([thruster]) == 0:
            pass

def calculate_loop(program, setting):
    amp_input = 0
    amps = [processor(program.copy()) for x in setting]
    init_amps(amps, setting)

    while(True):
        for i, thruster in enumerate(setting):
            f = io.StringIO()

            ret = 0
            with redirect_stdout(f):
                ret = amps[i].run([amp_input])
                while ret == 0:
                    ret = amps[i].run([amp_input])

            amp_input = int(f.getvalue())
            print("Out: {}".format(amp_input))

            if ret == 99:
                return amp_input

    return amp_input

if __name__ == "__main__":
    with open(FILE) as file:
        program = [int(x) for x in file.read()[:-1].split(",")]
        print(program)


#    solutions = []
#    for setting in itertools.permutations([0, 1, 2, 3, 4]):
#        out = calculate_out(program, setting)
#        solutions.append(out)
#
#    print("Solution 1: {}".format(max(solutions)))

    calculate_loop(program, [5, 6, 7, 8, 9])
