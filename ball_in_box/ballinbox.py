import math
import random
from .validate import validate

__all__ = ['ball_in_box']
def area_sum_c(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    #brute force 100 times
    best_circles = []
    best_ans=0
    blockers_l=len(blockers)
    generate_three=lambda : [random.random()*2 - 1,random.random()*2 - 1,random.random()**blockers_l]

    tim=(int)(5000/((m/5)**(math.log(6,2))))
    for iter in range(tim):
        current_circles = []
        for circle_index in range(m):

            [x,y,r]=generate_three()

            current_circles.append((x, y, r))
            while not validate(current_circles, blockers):
                [x, y, r] =generate_three()
                current_circles[circle_index] = (x, y, r)

            circle_index += 1
        current_sum=area_sum_c(current_circles)
        if current_sum > best_ans:
                best_circles=current_circles
                best_ans=current_sum

    return best_circles
