#!/usr/bin/python3

from pyrob.api import *


def seeking_for_hole():
    while wall_is_beneath():
        move_left()
        if wall_is_on_the_left():
            break
        # if not wall_is_beneath():
            # side_length = 1


def moving_right_for_wall():
    while not wall_is_on_the_right():
        move_right()
        if wall_is_on_the_left():
            break


def drop_down():
    while not wall_is_beneath():
        move_down()
        if wall_is_on_the_left():
            break


@task(delay=0.01)
def task_8_30():

    flag = True
    while flag:
        drop_down()

        moving_right_for_wall()
        seeking_for_hole()
        drop_down()
        if wall_is_on_the_left():
            break

    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
