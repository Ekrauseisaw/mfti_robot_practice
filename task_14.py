#!/usr/bin/python3

from pyrob.api import *


def fill_up():
    move_up(1)
    fill_cell()
    move_down(1)


def fill_down():
    move_down(1)
    fill_cell()
    move_up(1)


def fill_everything():
    if not wall_is_beneath() and not wall_is_above():
        fill_up()
        fill_down()

    elif not wall_is_beneath():
        fill_down()

    elif not wall_is_above():
        fill_up()

    elif wall_is_above() and wall_is_beneath():
        fill_cell()


@task
def task_8_11():
    while not wall_is_on_the_right():
        fill_everything()
        move_right()

    fill_everything()


if __name__ == '__main__':
    run_tasks()
