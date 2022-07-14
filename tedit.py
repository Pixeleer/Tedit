from glob import glob
import time
import random
import os
import string
from t_load import *

lvl_name = input("Level name >> ")

if os.path.exists(lvl_name+".tlvl") != True:
    print("Error: Level does not exist.")
    os.system("pause")
    exit()

import turtle

t = turtle.Turtle()

the_turtle = turtle

class global_shit:
    times = 0
    looping = False
    done = False
    skip = False
    c = False
    loops_complete = []

t_load.load(t, the_turtle, lvl_name, global_shit)

print(str(global_shit.looping))
while global_shit.looping:
    t_load.load(t, the_turtle, lvl_name, global_shit)
    if not global_shit.looping:
        break

if global_shit.done == True:
    os.system("pause")
    exit()