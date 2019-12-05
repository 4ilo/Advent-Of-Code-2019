
class processor:
    def __init__(self, program):
        self.program = program
        self.ip = 0

    def run(self):
        instruction = self.program[self.ip]
        self.ip += 1

        opcode = int(str(instruction)[-2:])
        modes = [int(x) for x in list(str(instruction)[:-2])[::-1]]

        if opcode == 1:
            self.add(modes)
            self.ip += 3

        elif opcode == 2:
            self.multiply(modes)
            self.ip += 3

        elif opcode == 3:
            self.inp(modes)
            self.ip += 1

        elif opcode == 4:
            self.outp(modes)
            self.ip += 1

        elif opcode == 5:
            self.jump_t(modes)

        elif opcode == 6:
            self.jump_f(modes)

        elif opcode == 7:
            self.less_then(modes)
            self.ip += 3

        elif opcode == 8:
            self.equal(modes)
            self.ip += 3

        elif opcode == 99:
            #print(self.program)
            return 99

        else:
            print("Invalid instruction: [{}]: {}".format(self.ip-1, instruction))
            return -1

        return 0

    def value(self, offset, mode):
        if mode:
            # immediate mode
            return self.program[self.ip + offset]
        else:
            # position mode
            return self.program[self.program[self.ip + offset]]

    def jump_t(self, modes):
        if len(modes) < 2:
            modes += [0] * (3 - len(modes))

        if self.value(0, modes[0]):
            self.ip = self.value(1, modes[1])
        else:
            self.ip += 2

    def jump_f(self, modes):
        if len(modes) < 2:
            modes += [0] * (3 - len(modes))

        if not self.value(0, modes[0]):
            self.ip = self.value(1, modes[1])
        else:
            self.ip += 2

    def less_then(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        if self.value(0, modes[0]) < self.value(1, modes[1]):
            self.program[self.program[self.ip + 2]] = 1
        else:
            self.program[self.program[self.ip + 2]] = 0

    def equal(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        if self.value(0, modes[0]) == self.value(1, modes[1]):
            self.program[self.program[self.ip + 2]] = 1
        else:
            self.program[self.program[self.ip + 2]] = 0


    def add(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        self.program[self.program[self.ip + 2]] = self.value(0, modes[0]) + self.value(1, modes[1])

    def multiply(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        self.program[self.program[self.ip + 2]] = self.value(0, modes[0]) * self.value(1, modes[1])

    def inp(self, modes):
        self.program[self.program[self.ip]] = int(input("ID:"))

    def outp(self, modes):
        if len(modes) < 1:
            modes += [0] * (3 - len(modes))

        print(self.value(0, modes[0]))
