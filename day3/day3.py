#!/usr/bin/python3

#FILE = "example.txt"
FILE = "input.txt"

def track(field, wire):
    px = 0
    py = 0
    length = 0

    for section in wire:

        if section[0] == "R":
            for x in range(int(section[1:])):
                px += 1
                length += 1

                if (py, px) in field:
                    field[(py, px)][0] += 1
                else:
                    field.update({(py, px): [1, length]})

        if section[0] == "U":
            for x in range(int(section[1:])):
                py -= 1
                length += 1

                if (py, px) in field:
                    field[(py, px)][0] += 1
                else:
                    field.update({(py, px): [1, length]})

        if section[0] == "L":
            for x in range(int(section[1:])):
                px -= 1
                length += 1

                if (py, px) in field:
                    field[(py, px)][0] += 1
                else:
                    field.update({(py, px): [1, length]})

        if section[0] == "D":
            for x in range(int(section[1:])):
                py += 1
                length += 1

                if (py, px) in field:
                    field[(py, px)][0] += 1
                else:
                    field.update({(py, px): [1, length]})


if __name__ == "__main__":
    with open(FILE) as file:
        wire1 = file.readline()[:-1].split(",")
        wire2 = file.readline()[:-1].split(",")


    field1 = {}
    field2 = {}

    track(field1, wire1)
    field1 = {k: v for k, v in field1.items() if v[0] == 1}

    track(field2, wire2)
    field2 = {k: v for k, v in field2.items() if v[0] == 1}

    for key, value in field1.items():
        if key in field2:
            field1[key][0] += 1
            field1[key][1] += field2[key][1]

    distance = sorted([(abs(k[0]) + abs(k[1])) for k, v in field1.items() if v[0] > 1])
    print("Result 1: {}".format(distance[0]))

    steps = sorted([v[1] for k, v in field1.items() if v[0] > 1])
    print("Result 2: {}".format(steps[0]))

