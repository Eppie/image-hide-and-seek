#!/usr/bin/python

from heapq import heappush, heappop
from PIL import Image
import random

random.seed(1)


def dist(x, y):
    return sum([(x[i] - y[i]) ** 2 for i in range(3)])


def gradient_descent(image_name, c, SAVE_IMAGES=False):
    im = Image.open('images/' + image_name + '.jpg').convert('RGB')
    L = im.load()
    sx, sy = im.size
    heap = []
    visited = set()
    count = 0
    iters_between_save = 10000
    # color_to_set = (255 - c[0], 255 - c[1], 255 - c[2])
    color_to_set = (0, 255, 0)
    points = []
    for i in range(0, sx, sx / 98):
        for j in range(0, sy, sy / 98):
            points.append((i, j))
    for x in points:
        heappush(heap, [dist(c, L[x[0], x[1]]), [x[0], x[1]]])
        visited.add((x[0], x[1]))

    while heap:
        if count % 10 == 0:
            x = random.random()
            if x < 0.5:
                n = heap.pop(random.randint(10, 100))
            else:
                n = heappop(heap)
        else:
            n = heappop(heap)
        x, y = n[1]
        c_color = L[x, y]
        count += 1
        L[x, y] = color_to_set

        if c_color == c:
            p = float(len(visited)) / (sx * sy) * 100
            print('color: {}, count: {} / {}%, position: {}'.format(c, len(visited), p, (x, y)))
            if SAVE_IMAGES:
                im.save(image_name + '_' + str(c[0]) + '_' + str(c[1]) + '_' + str(c[2]) + '_' + '{:05}'.format((count / iters_between_save) + 1) + '.png')
            return len(visited)

        if count % iters_between_save == 0:
            p = float(count) / (sx * sy) * 100
            print('position: {}, dist: {}, count: {}, visited %: {}, heap size: {}'.format((x, y), dist(c, c_color), count, p, len(heap)))
            if SAVE_IMAGES:
                im.save(image_name + '_' + str(c[0]) + '_' + str(c[1]) + '_' + str(c[2]) + '_' + '{:05}'.format(count / iters_between_save) + '.png')

        newpoints = []
        newpoints.append((x + 1, y))
        newpoints.append((x - 1, y))
        newpoints.append((x, y + 1))
        newpoints.append((x, y - 1))
        newpoints.append((x + 1, y + 1))
        newpoints.append((x + 1, y - 1))
        newpoints.append((x - 1, y + 1))
        newpoints.append((x - 1, y - 1))

        for p in newpoints:
            if p not in visited:
                try:
                    d = dist(c, L[p[0], p[1]])
                    heappush(heap, [d, [p[0], p[1]]])
                    visited.add(p)
                except IndexError:
                    pass


def linear_search(image_name, c):
    im = Image.open('images/' + image_name + '.jpg').convert('RGB')
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
    im = Image.open('images/' + image_name + '.jpg').convert('RGB')
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
