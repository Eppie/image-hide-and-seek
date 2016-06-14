#!/usr/bin/python

from PIL import Image


def dist(x, y):
    return sum([(x[i] - y[i]) ** 2 for i in range(3)])


def mid(x, y):
    return (x + y) / 2


class Finder:
    def __init__(self, image_name, c):
        self.image_name = image_name,
        self.c = c
        self.found = False
        self.position = None
        self.im = Image.open(image_name + ".jpg").convert("RGB")
        self.L = self.im.load()
        self.sx, self.sy = self.im.size
        self.im.close()
        self.visited = set()

    def quadsearch(self, x0, x1, y0, y1):
        if x0 == x1 and y0 == y1:
            return
        xm = mid(x0, x1)
        ym = mid(y0, y1)
        R = [
            (x0, xm, y0, ym),
            (xm, x1, y0, ym),
            (x0, xm, ym, y1),
            (xm, x1, ym, y1),
        ]
        P = [(mid(t[0], t[1]), mid(t[2], t[3])) for t in R]
        DR = []
        for i in range(len(P)):
            p = P[i]
            if p in self.visited:
                continue
            self.visited.add(p)
            u = self.L[p[0], p[1]]
            d = dist(u, self.c)
            if d == 0:
                self.found = True
                self.position = (p[0], p[1])
                return
            DR.append((d, R[i]))
        S = sorted(range(len(DR)), key=lambda k: DR[k][0])
        for i in S:
            if self.found:
                return
            r = DR[i][1]
            self.quadsearch(r[0], r[1], r[2], r[3])

    def start(self):
        self.quadsearch(0, self.sx, 0, self.sy)

    def result(self):
        if self.found:
            count = len(self.visited)
            ratio = float(count) / (self.sx * self.sy)
            print len(self.visited), ratio, self.position, self.L[self.position[0], self.position[1]], "=", self.c
            return count
        else:
            print self.c, "not found"
            return 0

if __name__ == "__main__":
    image_name = "turret-arch"
    c = (116, 70, 36)
    F = Finder(image_name, c)
    F.start()
    F.result()
