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

def find_path(objects, search, stop, path=[]):
    p = path.copy()
    if search == stop:
        return p

    obj = objects.pop(search, None)
    p.append(search)
    if not obj:
        return False

    for orbit in obj:
        ret = find_path(objects, orbit, stop, p)
        if ret != False:
            return ret

    return False

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

    # Plot the path to YOU and SAN
    path1 = find_path(objects.copy(), "COM", "YOU")
    path2 = find_path(objects.copy(), "COM", "SAN")

    # Find the length of the common part
    common_part = len(list(set(path1) & set(path2)))
    distance = len(path1) + len(path2) - (2 * common_part)

    print("Result 2: {}".format(distance))
