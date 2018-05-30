import math
import random

__all__ = ['ball_in_box']


def area_sum_c(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area


def max_residue_distance(tup,circles): #计算圆能增长的最大半径
    res = float('inf')
    x = tup[0]
    y = tup[1]

    if x <= -1 or x >= 1 or y <= -1 or y >= 1:
        return 0
    else:
        res = min(res, 1-x, x+1, 1-y, y+1)
    for circle in circles:
        res = min(res, math.sqrt((circle[0] - x)**2 + (circle[1] - y)**2) - circle[2])
        if res <= 0:
            return 0
    return res


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    best_circles = []
    if m == 0:  # ugly
        return best_circles
    best_sum = 0
    blockers_l=len(blockers)
    init_circle=[]
    for tup in blockers:
        init_circle.append((tup[0],tup[1],0))  # blockers 当做 半径0气球

    generate_three = lambda: (random.random()*2 - 1,random.random()*2 - 1, 0)  # 随机生成圆(半径为0)

    tim =(int)(500000/(pow(m,1.65)))  # 迭代次数
    # tim=10000000
    # print(tim)
    if tim == 0:  # 如果m非常大
        tim = 1
    for _ in range(tim):
        current_circles = init_circle[:]
        while True:
            x, y, _ = generate_three()

            dis = max_residue_distance((x, y, 0), current_circles) - 0.0000000001  # precision control like cpp

            if dis > 0:
                current_circles.append((x, y, dis))
                if len(current_circles) >= m + blockers_l:
                    break
        current_sum = area_sum_c(current_circles)
        if current_sum > best_sum:
            best_circles = current_circles
            best_sum = current_sum
    return best_circles[blockers_l:]
