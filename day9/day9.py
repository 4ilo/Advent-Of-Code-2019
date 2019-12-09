#!/usr/bin/python3

import io
from processor import processor
from contextlib import redirect_stdout

FILE = "example.txt"
FILE = "input.txt"

def run(program, inp_data, mem_size=10000):
    cpu = processor(program, mem_size)

    f = io.StringIO()

    with redirect_stdout(f):
        data = [inp_data]
        while cpu.run(data) == 0:
            pass

    return int(f.getvalue())

if __name__ == "__main__":
    with open(FILE) as file:
        program = [int(x) for x in file.read().split(",")]
#        print(program)


    result = run(program, 1)
    print("Result 1: {}".format(result))

    result = run(program, 2)
    print("Result 2: {}".format(result))
