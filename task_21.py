#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for values in range(1, 14):
        for y in range(values):
            fill_cell()
            move_right()

        for y in range(values):
            move_left()
        move_down()



if __name__ == '__main__':
    run_tasks()
