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


def func(x, a, b): #拟合的函数
    return a*pow(x,b)


if __name__ == '__main__':

    x=[] #用来收集圆圈数目
    y=[] #用来收集时间

    for i in range(1):
        start = time.clock()
        ii = i*100+1
        num_of_circle = ii
        x.append(ii)
        # blockers = [(0.5, 0.5), (-0.5, -0.5), (0.5, 0.3),[-0.3,0.9],[0.1,0.1],[0.2,0.2],[-0.1,-0.1]]
        blockers = []

        circles = bb.ball_in_box(num_of_circle, blockers)

        if num_of_circle == len(circles) and val.validate(circles, blockers):
            area = area_sum(circles)
            print("Total area: {}".format(area))
            y.append(time.clock()-start)
            fig, ax = plt.subplots()
            plt.xlim((-1, 1))
            plt.ylim((-1, 1))
            for circle in circles:
                ax.add_artist(plt.Circle((circle[0], circle[1]), circle[2]))
            for blocker in blockers:
                ax.add_artist(plt.Circle((blocker[0], blocker[1]), 0.01, color='r'))
            plt.savefig("../src/m="+str(ii)+".png")
            plt.show()
            plt.gcf().clear()
        else:
            print("Error: no good circles.")

    print(y)




#以下是拟合,时间复杂度部分
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




