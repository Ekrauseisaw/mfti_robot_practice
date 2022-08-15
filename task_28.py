#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    flag = True
    filled_cells = []
    while flag:
        move_right()
        if cell_is_filled():
            filled_cells.append("x")
        if len(filled_cells) == 5:
            flag = False


    #n = 0
    #while not n == 5:
        #move_right()
        #if cell_is_filled():
            #n += 1


if __name__ == '__main__':
    run_tasks()
