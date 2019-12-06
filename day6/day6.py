#!/usr/bin/python3

#FILE = "example.txt"
#FILE = "example2.txt"
FILE = "input.txt"

def count(objects, search, steps=0):
    total = 0
    obj = objects.pop(search, None)
    if not obj:
        return steps

    total += steps
    steps += 1

    for orbit in obj:
        total += count(objects, orbit, steps)

    return total

def path(objects, search, stop, steps=0):
    path = []
    total = 0
    if search == stop:
        return steps

    obj = objects.pop(search, None)
    path.append(obj)
    if not obj:
        return 0

    steps += 1

    for orbit in obj:
        total += path(objects, orbit, stop, steps)

    return total

def common(

if __name__ == "__main__":
    with open(FILE) as file:
        data = file.read().splitlines()
        print(data)

    objects = {}

    for line in data:
        line = line.split(")")

        if line[0] not in objects:
            objects.update({line[0]: [line[1]]})

        else:
            objects[line[0]].append(line[1])


    total = count(objects.copy(), "COM")
    print("Result 1: {}".format(total))

    path1 = path(objects.copy(), "COM", "YOU") -1
    print(path1)
    path2 = path(objects.copy(), "COM", "SAN") -1
    print(path2)

    dif = abs(path1 - path2) + 1
    print(dif)
    path1 = (path1-dif) + (path2-dif)
    print("Result 2: {}".format(path1))


