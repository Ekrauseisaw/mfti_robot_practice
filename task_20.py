#!/usr/bin/python3

from pyrob.api import *


def move_right_and_fill():
    move_right()
    fill_cell()


def move_left_and_fill():
    move_left()
    fill_cell()


def move_down_and_fill():
    move_down()
    fill_cell()


def moving_rightside():
    for i in range(26):
        move_right_and_fill()
    move_down_and_fill()


def moving_leftside():
    for i in range(26):
        move_left_and_fill()
    move_down_and_fill()


@task(delay=0.05)
def task_4_3():
    for i in range(27):
        move_right_and_fill()
    move_down_and_fill()

    for x in range(5):
        moving_leftside()
        moving_rightside()

    for y in range(26):
        move_left_and_fill()
    move_down()


if __name__ == '__main__':
    run_tasks()
