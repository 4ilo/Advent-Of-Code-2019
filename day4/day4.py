#!/usr/bin/python3

import re

RANGE = (357253, 892942)

def validate(password, part2=False):
    pass_str = str(password)

    # 2 adjacent letters are the same
    matches = re.findall(r"(.)\1", pass_str)
    if not matches:
        return 0
    elif part2:
        ok = False

        for match in matches:
            if pass_str.count(match) == 2:
                ok = True

        if not ok:
            return 0

    # Digits should never decrease from left to right
    for i, c in enumerate(pass_str):
        if i < 5 and int(c) > int(pass_str[i + 1]):
            return 0

    return 1

if __name__ == "__main__":
    # Part 1 examples
    should_pass = [122345, 111111]
    should_fail = [223450, 123789]

    for passw in should_pass:
        if not validate(passw):
            print("[{}] Should have passed.".format(passw))

    for passw in should_fail:
        if validate(passw):
            print("[{}] Should have failed.".format(passw))

    # Part 2 examples
    should_pass = [112233, 111122]
    should_fail = [123444]

    for passw in should_pass:
        if not validate(passw, part2=True):
            print("[{}] Should have passed.".format(passw))

    for passw in should_fail:
        if validate(passw, part2=True):
            print("[{}] Should have failed.".format(passw))


    # Soluton part 1
    counter = 0
    for i in range(RANGE[0], RANGE[1]):
        counter += validate(i)

    print("Result 1: {}".format(counter))

    # Soluton part 2
    counter = 0
    for i in range(RANGE[0], RANGE[1]):
        counter += validate(i, part2=True)

    print("Result 2: {}".format(counter))
