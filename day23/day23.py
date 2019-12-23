import io
from processor import processor
from contextlib import redirect_stdout

FILE = "input.txt"

queue = {}
last = 0


def init_nics(amount, program):
    nics = []
    for i in range(amount):
        data = [i]
        nic = processor(program.copy(), 10000)
        queue[i] = []
        while nic.run(data) == 0:
            pass

        nics.append(nic)
    return nics


def get_value(nic):
    if len(queue[nic]):
        val = queue[nic]
        queue[nic] = []
        return val

    return [-1]


def do_all(nics):
    global last
    idle = True
    for i in range(len(nics)):
        f = io.StringIO()
        with redirect_stdout(f):
            data = get_value(i)
            if data != [-1]:
                idle = False
            ret = nics[i].run(data)
            while ret == 0:
                ret = nics[i].run(data)

        out = f.getvalue()
        out = [int(x) for x in out.split("\n")[:-1]]
        out = [out[i:i + 3] for i in range(0, len(out), 3)]
        #print(out)
        for packet in out:
            if packet[0] == 255:
                if 255 not in queue:
                    print("Result 1: {}".format(packet[2]))
                queue[255] = packet[1:]

            else:
                queue[packet[0]] += packet[1:]

    if idle:
        queue[0] = queue[255]
        if queue[255][1] == last:
            print("Result 2: {}".format(last))
            exit()
        last = queue[0][1]


if __name__ == "__main__":
    with open(FILE) as file:
        program = [int(x) for x in file.read()[:-1].split(",")]
        # print(program)

        nics = init_nics(50, program)

        while True:
            do_all(nics)

