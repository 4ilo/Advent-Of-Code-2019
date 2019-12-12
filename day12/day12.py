#!/usr/bin/python3

import re
import itertools
from math import gcd

steps = 1000
FILE = "example.txt"
FILE = "input.txt"

regexp = "<x=(-?\d+), y=(-?\d+), z=(-?\d+)>"


class Moon:
    def __init__(self, position):
        self.pos = [int(position[0]), int(position[1]), int(position[2])]
        self.vel = [0, 0, 0]

    def __str__(self):
        return "pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(*self.pos, *self.vel)

    def apply_gravity(self, moon2):
        for axis in range(3):
            if self.pos[axis] > moon2.pos[axis]:
                moon2.vel[axis] += 1
                self.vel[axis] -= 1
            elif self.pos[axis] < moon2.pos[axis]:
                moon2.vel[axis] -= 1
                self.vel[axis] += 1

    def update_pos(self):
        for axis in range(3):
            self.pos[axis] += self.vel[axis]

    def energy(self):
        pot = 0
        kin = 0
        for axis in range(3):
            pot += abs(self.pos[axis])
            kin += abs(self.vel[axis])

        return pot, kin


def step(moons):
    """ Move all moons 1 step"""
    for moon1, moon2 in itertools.combinations(moons, 2):
        moon1.apply_gravity(moon2)

    for moon in moons:
        moon.update_pos()


def calc_energy(moons):
    total_energy = 0
    for moon in moons:
        energy = moon.energy()
        total_energy += energy[0] * energy[1]

    return total_energy


def repetition_len(moons, axis):
    counter = 0
    initial = tuple([x.pos[axis] for x in moons] + [x.vel[axis] for x in moons])

    while True:
        counter += 1

        step(moons)
        pos = tuple([x.pos[axis] for x in moons] + [x.vel[axis] for x in moons])

        if pos == initial:
            return counter


def read_input():
    moons = []
    with open(FILE) as file:
        data = file.read().splitlines()
        for line in data:
            match = re.findall(regexp, line)
            if match:
                moon = Moon(match[0])
                moons.append(moon)

    return moons


def least_common_multiple(lengths):
    lcm = lengths[0]

    for i in lengths[1:]:
        lcm = lcm * i // gcd(lcm, i)

    return lcm


if __name__ == "__main__":
    moons = read_input()

    # Part 1
    for i in range(steps):
        step(moons)

    energy = calc_energy(moons)
    print("Result 1: {}".format(energy))

    # Part 2
    lengths = []
    for axis in range(3):
        moons = read_input()
        lengths.append(repetition_len(moons, axis))

    print("Solution2: {}".format(least_common_multiple(lengths)))


