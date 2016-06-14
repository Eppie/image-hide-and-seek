#!/usr/bin/python

from PIL import Image
import random

random.seed(99237586238472)


def linear_search(image_name, c):
    im = Image.open(image_name + '.jpg').convert('RGB')
    L = im.load()
    sx, sy = im.size
    count = 0
    for i in range(sx):
        for j in range(sy):
            count += 1
            if c == L[i, j]:
                p = float(count) / (sx * sy) * 100
                print('count: {}, percent: {}, position: {}'.format(count, p, (i, j)))
                return count
    return 0


def random_search(image_name, c):
    im = Image.open(image_name + '.jpg').convert('RGB')
    L = im.load()
    sx, sy = im.size
    count = 0
    x_list = range(sx)
    y_list = range(sy)
    random.shuffle(x_list)
    random.shuffle(y_list)
    for i in x_list:
        for j in y_list:
            count += 1
            if c == L[i, j]:
                p = float(count) / (sx * sy) * 100
                print('count: {}, percent: {}, position: {}'.format(count, p, (i, j)))
                return count
    return 0
