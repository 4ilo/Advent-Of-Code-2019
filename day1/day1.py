#!/usr/bin/python3

import math

#FILE = "example.txt"
FILE = "input.txt"

def required_fuel(mass):
    return math.floor(mass/3) - 2

def required_fuel_fuel(mass):
    total = 0

    while (1):
        mass = required_fuel(mass)
        if (mass <= 0):
            return total
        else:
            total += mass

if __name__ == "__main__":
    with open(FILE) as file:
        input = file.read().split("\n")
        input = [int(x) for x in input[:-1]]

    # Part 1
    fuel = 0
    for mass in input:
        fuel += required_fuel(mass)

    print("Solution 1: {}".format(fuel));

    # Part 2
    total_fuel = 0
    for mass in input:
        total_fuel += required_fuel_fuel(mass)

    print("Solution2: {}".format(total_fuel))
