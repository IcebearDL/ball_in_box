import math
import random
from time import sleep

__all__ = ['ball_in_box']



def max_residue_distance(tup,circles): #计算某一个确定圆心能增长的最大半径
    res = float('inf')
    x,y = tup[0], tup[1]
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
    blockers_l=len(blockers)
    generate_pair_random = lambda x,y,fix: (x+fix*(random.random()*2-1),y+fix*(random.random()*2-1))  # 按中心位置随机生成圆位置(半径为0)
    J_function = lambda circles:sum([math.pi*circle[2]**2 for circle in circles])
    init_cirs = [(tup[0],tup[1],0) for tup in blockers]  # blockers当做气球
    best_value = 0
    best_circles_all = 0,0,0
    for __ in range(200):
        cur_cirs = init_cirs[:]
        while len(cur_cirs) < blockers_l + m:
            best_circle = [0,0,0]
            for k in range(2):  # 基本上可以证明贪心是错误的,k是迭代次数,在一片区域寻找,然后在最优解的附近一个格子范围继续寻找
                i = 0  # radius
                better_circle = [0,0,0]
                while i <= 1000 or better_circle[2] == 0:
                    tmp_pos = generate_pair_random(best_circle[0], best_circle[1], 0.02**k)
                    tmp = max_residue_distance(tmp_pos,cur_cirs)
                    if better_circle[2] < tmp :
                        better_circle[2] = tmp
                        better_circle[0],better_circle[1] =tmp_pos
                    i+=1
                best_circle=better_circle
            cur_cirs.append(tuple(best_circle))
        cost = J_function(cur_cirs)
        if cost > best_value:
            best_value = cost
            best_circles_all = cur_cirs

    return best_circles_all[blockers_l:]
