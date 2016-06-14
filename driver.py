#!/usr/bin/python

import Eppie
import Karl


def run_random_search(image_name, c):
    return Eppie.random_search(image_name, c)


def run_linear_search(image_name, c):
    return Eppie.linear_search(image_name, c)


def run_quadsearch(image_name, c):
    F = Karl.Finder(image_name, c)
    F.start()
    return F.result()


def run(func):
    total_count = 0
    with open('tests', 'r') as f:
        num_images = int(f.readline())
        for _ in range(num_images):
            image_name = f.readline().strip()
            num_tests = int(f.readline())
            for _ in range(num_tests):
                c = tuple(map(int, f.readline().split()))
                total_count += func(image_name, c)
    print total_count

run(run_random_search)
