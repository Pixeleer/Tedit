from glob import glob
import time
import random
import os
import string

lvl_name = input("Level name >> ")

if os.path.exists(lvl_name+".tlvl") != True:
    print("Error: Level does not exist.")
    os.system("pause")
    exit()

class global_shit:
    times = 0
    looping = False
    done = False
    skip = False
    c = False

    loops_complete = []

import turtle

t = turtle.Turtle()

def load():
    try:
        with open(lvl_name+".tlvl", "r") as lvl:
            c_sep = lvl.read().split(",")

            for item in c_sep:
                value = item.split(":")

                pixels, direction = value[1], value[0]

                if global_shit.c == True:
                    if direction != "c":
                        continue
                    else:
                        global_shit.c = False

                if pixels == "random":
                        num = random.randint(1, 400)

                        pixels = str(num)

                if pixels == "randpos":
                        num1 = random.randint(-640, 640)
                        num2 = random.randint(-540, 540)

                        pixels = str(num1)+";"+str(num2)

                if direction == "loop":
                    global_shit.looping = True

                if direction == "penc":
                    t.pencolor(pixels)

                if direction == "cls":
                    t.clear()

                if direction == "spd":
                    t.speed(int(pixels))

                if direction == "w":
                    turtle.delay(int(pixels))

                if direction == "u":
                    t.up()

                if direction == "d":
                    t.down()

                if direction == "goto":
                    splitting = pixels.split(";")

                    x, y = splitting[0], splitting[1]

                    t.goto(float(x), float(y))

                if direction == "wrd":
                    t.write(pixels)

                if direction == "c":
                    global_shit.looping = True
                    continue

                if direction == "gtc":
                    global_shit.c = True
                    continue

                if direction == "endl":
                    global_shit.looping = False

                if direction == "1":
                    t.forward(int(pixels))

                if direction == "2":
                    t.back(int(pixels))

                if direction == "3":
                    t.right(int(pixels))
                    
                if direction == "4":
                    t.left(int(pixels))
            

    except Exception as e:
        print("Error: Level data is corrupted.")
        print("Traceback:\n"+str(e))
        os.system("pause")
                    
load()

while global_shit.looping:
    load()
    if not global_shit.looping:
        break

global_shit.done = True
turtle.done()

if global_shit.done == True:
    os.system("pause")
    exit()