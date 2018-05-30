import math
import time
import ball_in_box.ballinbox as bb
import ball_in_box.validate as val
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area


def func(x, a, b):
    return a*pow(x,b)


if __name__ == '__main__':

    x=[]
    y=[]
    for i in range(20):
        start = time.clock()
        num_of_circle = i+5
        x.append(i+5)
        blockers = [(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]
        # blockers = []

        circles = bb.ball_in_box(num_of_circle, blockers)

        if num_of_circle == len(circles) and val.validate(circles, blockers):
            area = area_sum(circles)
            print("Total area: {}".format(area))
            y.append(time.clock()-start)
        else:
            print("Error: no good circles.")

    print(y)
    # popt, pcov = curve_fit(func, x, y)
    # a = popt[0]
    # b = popt[1]
    # yvals = func(x, a, b)
    # print(a) #0.0001373
    # print(b) # 1.69845
    # plot1 = plt.plot(x, y, 's', label='original values')
    # plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.legend(loc=4)  # 指定legend的位置右下角
    # plt.title('curve_fit')
    # plt.savefig('test3.png')
    # plt.show()




