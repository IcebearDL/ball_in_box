import math
import numpy as np
import random
from itertools import product

__all__ = ['ball_in_box']


def dist(a,b): return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)  # 距离公式


def max_rediue(point,circles):
    rad = min(1 - point[0], point[0] + 1, 1 - point[1], point[1] + 1)
    for circle in circles:
        rad = min(rad, dist(point, circle) - circle[2])
        if rad < 0:
            return 0
    return rad


def J_function(circles):return sum([math.pi*circle[2]**2 for circle in circles])


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    points_list = list(product(np.linspace(-1, 1, 250), np.linspace(-1, 1, 250)))  # 点阵(随机也可以
    cur_circles = [(block[0],block[1],0) for block in blockers]  # blocker作为气球
    for i in range(m):
        maxcircle = 0, 0, 0
        for point in points_list:
            rad = max_rediue(point,cur_circles)
            if rad > maxcircle[2]:
                maxcircle = point[0],point[1],rad

        if i < 5:
            for __ in range(10000):
                delta = random.uniform(-1,1)/250
                tmpcircle = [maxcircle[0] + delta , maxcircle[1] + delta , 0]
                tmpr = max_rediue(tmpcircle, cur_circles)
                if tmpr > maxcircle[2]:
                    tmpcircle[2]=tmpr
                    maxcircle = tuple(tmpcircle)

        cur_circles.append(maxcircle)
        points_list = list(filter(lambda p: dist(p, maxcircle) >= maxcircle[2], points_list))
    solve_circles = cur_circles[len(blockers):]

    return solve_circles
