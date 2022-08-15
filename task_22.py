#!/usr/bin/python3

from pyrob.api import *


def right_side():
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
        # fill_cell()


def left_side():
    while not wall_is_on_the_left():
        fill_cell()
        move_left()


@task(delay=0.01)
def task_5_10():
    while not wall_is_beneath():
        #if wall_is_beneath() and wall_is_above():
            #fill_cell()
            #break
        right_side()
        left_side()
        move_down()

    if not wall_is_above():
        right_side()
        left_side()
    else:
        fill_cell()


if __name__ == '__main__':
    run_tasks()
