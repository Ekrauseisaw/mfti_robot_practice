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


def crossing_right_side():
    for i in range(9):
        cross()
        move_right(4)
    cross()


def crossing_left_side():
    for i in range(9):
        cross()
        move_left(4)
    cross()


def two_lines():
    move_down(4)
    crossing_left_side()

    move_down(4)
    crossing_right_side()


@task(delay=0.01)
def task_2_4():
    move_down()
    move_right()

    crossing_right_side()

    two_lines()

    two_lines()

    while not wall_is_on_the_left():
        move_left()
    move_up()


if __name__ == '__main__':
    run_tasks()
