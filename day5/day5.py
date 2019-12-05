#!/usr/bin/python3

from processor import processor

#FILE = "example.txt"
FILE = "input.txt"


if __name__ == "__main__":
    with open(FILE) as file:
        program = [int(x) for x in file.read()[:-1].split(",")]
        print(program)

    proc = processor(program)

    while(proc.run() == 0):
        pass

