#!/usr/bin/python3

from pyrob.api import *


def moving_to_top():
    ax = 0
    while not wall_is_above():
        move_up()
        if cell_is_filled():
            ax += 1
        else:
            fill_cell()

    while not wall_is_beneath():
        move_down()
    return ax


@task(delay=0.01)
def task_8_18():

    ax = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            ax += 1
        if wall_is_above():
            if not cell_is_filled():
                fill_cell()
        else:
            ax += moving_to_top()
        move_right()
        mov('ax', ax)


if __name__ == '__main__':
    run_tasks()
