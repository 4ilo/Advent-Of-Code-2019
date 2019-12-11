
class processor:
    def __init__(self, program, mem_size):
        self.program = program
        self.program += [0] * (mem_size - len(self.program))    # Create more memory space
        self.ip = 0
        self.rel_offset = 0

    def run(self, data):
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
            ret = self.inp(modes, data)
            if ret == -1:
                self.ip -= 1
                return ret
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

        elif opcode == 9:
            self.inc_offset(modes)
            self.ip += 1

        elif opcode == 99:
            #print(self.program)
            return 99

        else:
            print("Invalid instruction: [{}]: {}".format(self.ip-1, instruction))
            return -1

        return 0

    def value(self, offset, mode):
        if mode == 1:
            # immediate mode
            return self.program[self.ip + offset]
        elif mode == 2:
            # relative mode
            return self.program[self.rel_offset + self.program[self.ip + offset]]
        else:
            # position mode
            return self.program[self.program[self.ip + offset]]

    def write(self, offset, mode, dat):
        if mode == 2:
            # Relative mode
            self.program[self.rel_offset + self.program[self.ip + offset]] = int(dat)
        else:
            self.program[self.program[self.ip + offset]] = int(dat)

    def inc_offset(self, modes):
        if len(modes) < 1:
            modes += [0] * (1 - len(modes))
        self.rel_offset += self.value(0, modes[0])

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
            self.write(2, modes[2], 1)
        else:
            self.write(2, modes[2], 0)

    def equal(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        if self.value(0, modes[0]) == self.value(1, modes[1]):
            self.write(2, modes[2], 1)

        else:
            self.write(2, modes[2], 0)

    def add(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        value = self.value(0, modes[0]) + self.value(1, modes[1])
        self.write(2, modes[2], value)

    def multiply(self, modes):
        if len(modes) < 3:
            modes += [0] * (3 - len(modes))

        value = self.value(0, modes[0]) * self.value(1, modes[1])
        self.write(2, modes[2], value)

    def inp(self, modes, data):
        if len(data) == 0:
            return -1

        if len(modes) < 1:
            modes += [0] * (1 - len(modes))

        dat = data.pop(0)
        self.write(0, modes[0], dat)

    def outp(self, modes):
        if len(modes) < 1:
            modes += [0] * (1 - len(modes))

        print(self.value(0, modes[0]))
