import math
import time
import os
import sys
import signal
sys.path.append(os.getcwd())
import ball_in_box.ballinbox as bb
import ball_in_box.validate as val

user = os.getcwd().split('/')[-2]

class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        with open('../../result', 'a') as the_file:
            the_file.write(user +" timeout(>10s) \n")
            
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)


def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area


if __name__ == '__main__':
    num_of_circle = 5
    blockers = [(0.5, 0.5)
               ,(0.5, -0.3)]
    start = time.clock()
    
    with timeout(seconds = 10):
        save_stdout = sys.stdout
        sys.stdout = open('../../trash', 'a')
        circles = bb.ball_in_box(num_of_circle, blockers)
        sys.stdout = open('../../result', 'a')

    
    print(user,end=" ")
    if num_of_circle == len(circles) and val.validate(circles, blockers):
        area = area_sum(circles)
        print("area= "+str(area)+" time= "+str(time.clock()-start))
    else:
        print("got wrong circles")
