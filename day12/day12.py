#!/usr/bin/python3

import re
import copy
import itertools
from collections import defaultdict

FILE = "example.txt"
#FILE = "input.txt"

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

    def apply_gravity2(self, moon2, axis):
        if self.pos[axis] > moon2.pos[axis]:
            moon2.vel[axis] += 1
            self.vel[axis] -= 1
        elif self.pos[axis] < moon2.pos[axis]:
            moon2.vel[axis] -= 1
            self.vel[axis] += 1

    def update_pos(self):
        for axis in range(3):
            self.pos[axis] += self.vel[axis]

    def update_pos2(self, axis):
        self.pos[axis] += self.vel[axis]

    def energy(self):
        pot = 0
        kin = 0
        for axis in range(3):
            pot += abs(self.pos[axis])
            kin += abs(self.vel[axis])

        return pot, kin

def print_moons(moons):
    for moon in moons:
        print(moon)

def step(moons):
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

def serialise(moons):
    datas = []
    for moon in moons:
        data = tuple(moon.pos + moon.vel)
        datas.append(data)

    return tuple(datas)


def repitition_len(moons, axis):
    initial = tuple([x.pos[axis] for x in moons] + [0 for x in moons])
    print(initial)
    counter = 0

    while True:
        for moon1, moon2 in itertools.combinations(moons, 2):
            moon1.apply_gravity2(moon2, axis)

        for moon in moons:
            moon.update_pos2(axis)

        pos = tuple([x.pos[axis] for x in moons] + [0 for x in moons])
        if pos == initial:
            print(counter)
            #return counter

        counter += 1

def read_inp():
    moons = []
    with open(FILE) as file:
        data = file.read().splitlines()
        for line in data:
            match = re.findall(regexp, line)
            if match:
                moon = Moon(match[0])
                moons.append(moon)

    return moons

if __name__ == "__main__":
    moons = read_inp()

    steps = 10
    for i in range(steps):
        step(moons)
    energy = calc_energy(moons)
    print("Result 1: {}".format(energy))

    for x in range(3):
        moons = read_inp()
        test = repitition_len(moons, x)
        print(test)

