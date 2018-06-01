import math
import numpy as np
from itertools import product

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    dist = lambda a,b : math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)  # dis fomula
    pointsList = list(product(np.linspace(-1,1,250),np.linspace(-1,1,250)))  # grid mersh and you can also random ...
    circlesList = [(block[0],block[1],0) for block in blockers]
    for _ in range(m):
        maxCircle = 0,0,0  # tuple
        for point in pointsList:
            rad = min(1 - point[0], point[0] + 1, 1 - point[1] , point[1] + 1)
            for circle in circlesList:
                rad = min(rad, dist(point, circle) - circle[2])
            if rad > maxCircle[2]:
                maxCircle = point[0],point[1],rad
        circlesList.append(maxCircle) 
        pointsList = list(filter(lambda p: dist(p, maxCircle) >= maxCircle[2], pointsList))
    return circlesList[len(blockers):]
