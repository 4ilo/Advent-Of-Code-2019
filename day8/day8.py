#!/usr/bin/python3

import numpy as np

FILE = "example.txt"
width, height = (3, 2) 

FILE = "input.txt"
width, height = (25, 6)

if __name__ == "__main__":
    with open(FILE) as file:
        pixels = [int(x) for x in list(file.read())[:-1]]
#        print(pixels)

    layers = []
    num_layers = len(pixels) // (width*height)
    print(num_layers)

    image = np.asarray(pixels).reshape((num_layers, height, width))

    layer_info = []
    for layer in image:
        zeros = np.count_nonzero(layer==0)
        unique, counts = np.unique(layer, return_counts=True)
        occ = dict(zip(unique, counts))

        layer_info.append([zeros, occ[1]*occ[2]])

    layer_info = sorted(layer_info, key=lambda x: x[0])
    print("Result 1: {}".format(layer_info[0][1]))
