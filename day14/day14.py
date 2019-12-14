#!/usr/bin/python3

from collections import defaultdict

FILE = "example.txt"

rest = defaultdict(lambda: 0)

def find_needed(reqs, end, amount=1):
    if end == 'ORE':
        return amount

    req = reqs[end]
    print(req)

    needed = 0
    for dep in req["dep"]:
        needed += find_needed(reqs, dep[1], int(dep[0]))
        print(needed)
        rest[dep[1]] = int(req["amount"]) - int(dep[0])
        print(rest)

    return needed

if __name__ == "__main__":
    with open(FILE) as file:
        data = file.read().splitlines()
        #print(data)

    reactions = []
    for line in data:
        pre, post = line.split(" => ")
        post = tuple(post.split(" "))
        pre = [tuple(x.split(" ")) for x in pre.split(", ")]

        reactions.append([pre, post])


    reqs = {}
    for line in reactions:
        reqs.update({
            line[-1][1]: {
                "amount": line[-1][0],
                "dep": line[0]
            }
        })

    test = find_needed(reqs, "FUEL")
    print(test)
