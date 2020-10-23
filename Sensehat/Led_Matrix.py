#!/usr/bin/python3

from sense_hat import SenseHat
from time import sleep
import random as rand
import sys

sense = SenseHat()

while(True):
    hled=rand.randrange(0,8)
    vled=rand.randrange(0,8)
    r=rand.randrange(0,255)
    g=rand.randrange(0,255)
    b=rand.randrange(0,255)
    sense.set_pixel(hled,vled,[r,g,b])
    print("x:{} y:{} r:{} g:{} b:{}".format(hled,vled,r,g,b))
    sleep(float(sys.argv[1]))


sense.clear()
