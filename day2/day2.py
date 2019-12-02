#!/usr/bin/python3

#FILE = "example.txt"
FILE = "input.txt"

RESULT = 19690720

def compute(instructions, noun, verb):
    ip = 0
    input = instructions.copy()

    if FILE != "example.txt":
        input[1] = noun
        input[2] = verb

    while (input[ip] != 99):
        if (input[ip] == 1):
            input[input[ip + 3]] = input[input[ip + 1]] + input[input[ip + 2]]
            ip += 4

        elif (input[ip] == 2):
            input[input[ip + 3]] = input[input[ip + 1]] * input[input[ip + 2]]
            ip += 4

        else:
            print("Invalid instruction: [{}]: {}".format(ip, input[ip]))
            return -1

    return input[0]

if __name__ == "__main__":
    with open(FILE) as file:
        input = file.read()[:-1].split(",")
        input = [int(x) for x in input]
        print(input)

    # Part 1
    result = compute(input, 12, 2)
    print("Result1: {}".format(result))

    # Part 2
    for noun in range(99):
        for verb in range(99):
            result = compute(input, noun, verb)

            if result == RESULT:
                print("Result2: {}".format(100 * noun + verb))
