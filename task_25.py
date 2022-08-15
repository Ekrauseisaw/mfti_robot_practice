#!/usr/bin/python3

from pyrob.api import *


def cross():
    fill_cell()
    move_up()
    fill_cell()
    move_down()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right()


@task(delay=0.01)
def task_2_2():
    move_down(2)
    move_right()
    for i in range(4):
        cross()
        move_right(4)
    cross()
    move_left()
    move_up()


if __name__ == '__main__':
    run_tasks()
