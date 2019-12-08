#!/usr/bin/python3

import numpy as np
from PIL import Image

FILE = "example.txt"
width, height = (2, 2)

FILE = "input.txt"
width, height = (25, 6)

if __name__ == "__main__":
    with open(FILE) as file:
        pixels = [int(x) for x in list(file.read())[:-1]]
        print(pixels)

    layers = []
    num_layers = len(pixels) // (width*height)
    print(num_layers)

    image = np.asarray(pixels).reshape((num_layers, height, width))

    layer_info = []
    for layer in image:
        zeros = np.count_nonzero(layer==0)
        unique, counts = np.unique(layer, return_counts=True)
        occ = dict(zip(unique, counts))
        if not 1 in occ:
            occ.update({1: 0})
        if not 2 in occ:
            occ.update({2: 0})

        layer_info.append([zeros, occ[1]*occ[2]])

    layer_info = sorted(layer_info, key=lambda x: x[0])
    print("Result 1: {}".format(layer_info[0][1]))

    # Convert layers to transparant pillow images
    p_layers = []
    for l in range(num_layers):
        p_image = Image.new("RGBA", (width, height))
        p = p_image.load()
        for y in range(height):
            for x in range(width):
                pix = image[l][y][x]
                if pix == 0:
                    p[x, y] = (0, 0, 0, 255)
                if pix == 1:
                    p[x, y] = (255, 255, 255, 255)
                if pix == 2:
                    p[x, y] = (255, 255, 255, 0)

        p_layers.append(p_image)

    # Overlay the images and show the result
    background = Image.new("RGBA", (width, height), color='red')
    for p_layer in reversed(p_layers):
        background.paste(p_layer, (0, 0), p_layer)

    background.save("output.png")

