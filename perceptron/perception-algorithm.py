#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : Aug-04-19 14:39
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import os
import numpy as np
import math


def perception(samples, labels, theta=None, epoch=1):
    if theta is None:
        theta = len(samples[0]) * [0]
    theta = np.asarray(theta)
    for _ in range(epoch):
        for i, x in enumerate(samples):
            if labels[i] * np.dot(theta, x) <= 0:
                theta = np.add(theta, np.multiply(labels[i], x))
    return theta


def hw1(samples, labels, epoch=1):
    theta = len(samples[0]) * [0]
    theta = np.asarray(theta)
    # the first point that the algorithm sees is always considered a mistake
    theta = np.add(theta, np.multiply(labels[0], samples[0]))
    mistakes = 1  # 
    for _ in range(epoch):
        for i, x in enumerate(samples):
            if i == 0 and _ == 0:
                continue
            if labels[i] * np.dot(theta, x) <= 0:
                mistakes += 1
                theta = np.add(theta, np.multiply(labels[i], x))
            print("theta:", theta)
            print("mistakes:", mistakes)
    return theta


def hw2():
    # d = 2  # 2次后收敛
    d = 3  # 2次后收敛
    n = d  # n = d samples
    xs = []
    for t in range(n):
        x = [0] * d
        for i in range(d):
            if i == t:
                x[i] = math.cos(math.pi*(t+1))
            else:
                x[i] = 0
        xs.append(x)
    # print(xs)

    ys = [1] * d
    theta = [0] * d
    epoch = 4
    for e in range(epoch):
        for i, x in enumerate(xs):
            theta = perception([x], [ys[i]], theta)
            print(theta)


def main():
    """
    theta = [1, 1]
    sample = [2, 2]
    ret = np.dot(theta, sample)
    print(ret)
    """
    """
    # starts with data point  ?(1)
    x1 = [[-1, -1], [1, 0], [-1, 1.5]]
    y1 = [1, -1, 1]
    # starts with data point  ?(2)
    x2 = [[1, 0], [-1, 1.5], [-1, -1]]
    y2 = [-1, 1, 1]
    # theta = hw1(x2, y2, epoch=3)
    # print(theta)

    # 1.c
    x1 = [[-1, -1], [1, 0], [-1, 10]]
    y1 = [1, -1, 1]  # mistakes 4
    x2 = [[1, 0], [-1, 10], [-1, -1]]
    y2 = [-1, 1, 1]  # mistakes 1
    # theta = hw1(x2, y2, epoch=3)
    # theta = hw1(x1, y1, epoch=10)
    """
    hw2()


if __name__ == "__main__":
    main()
