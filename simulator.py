from objects import *
from variables import *
import thread, time
import random
'''
#################
Usercode Function
#################
'''

def SR_filter(listname, markertype):
    temporary_list = []
    for l in listname:
        if l.marker_type == markertype:
            temporary_list.append(l)
    listname = temporary_list
    return listname


def distance_orderer(listname):
    listname = sorted(listname, key = lambda Marker: Marker.distance)
    return listname


def swarmcode(number):
    while True:
        robot_list[number].motors[0].speed = -50.0
        robot_list[number].motors[1].speed = 50.0



def usercode0():
    time.sleep(10)
    while True:
        markers = R0.see()
        markers = SR_filter(markers, 'TOKEN')


        if len(markers) > 0:
            angle = markers[0].bearing.y
            print markers[0].marker_type
            print angle
            if angle > 10 and angle < 30:
                R0.motors[0].speed = -40
                R0.motors[1].speed = 40
            elif angle < -10 and angle > -30:
                R0.motors[0].speed = 40
                R0.motors[1].speed = -40
            elif angle < 10 and angle > -10:
                R0.motors[0].speed = 50
                R0.motors[1].speed = 50
        else:
            R0.motors[0].speed = -100
            R0.motors[1].speed = 100

def usercode1():
    time.sleep(10)
    while True:
        markers = R1.see()
        markers = SR_filter(markers, 'TOKEN')


        if len(markers) > 0:
            angle = markers[0].bearing.y
            print markers[0].marker_type
            print angle
            if angle > 10 and angle < 30:
                R1.motors[0].speed = -40
                R1.motors[1].speed = 40
            elif angle < -10 and angle > -30:
                R1.motors[0].speed = 40
                R1.motors[1].speed = -40
            elif angle < 10 and angle > -10:
                R1.motors[0].speed = 50
                R1.motors[1].speed = 50
        else:
            R1.motors[0].speed = -100
            R1.motors[1].speed = 100

def usercode2():
    time.sleep(10)
    while True:
        markers = R2.see()
        markers = SR_filter(markers, 'TOKEN')

        if len(markers) > 0:
            angle = markers[0].bearing.y
            print markers[0].marker_type
            print angle
            if angle > 10 and angle < 30:
                R2.motors[0].speed = -40
                R2.motors[1].speed = 40
            elif angle < -10 and angle > -30:
                R2.motors[0].speed = 40
                R2.motors[1].speed = -40
            elif angle < 10 and angle > -10:
                R2.motors[0].speed = 50
                R2.motors[1].speed = 50
        else:
            R2.motors[0].speed = -100
            R2.motors[1].speed = 100

def usercode3():
    time.sleep(10)
    while True:
        markers = R3.see()
        markers = SR_filter(markers, 'TOKEN')

        if len(markers) > 0:
            angle = markers[0].bearing.y
            print markers[0].marker_type
            print angle
            if angle > 10 and angle < 30:
                R3.motors[0].speed = -40
                R3.motors[1].speed = 40
            elif angle < -10 and angle > -30:
                R3.motors[0].speed = 40
                R3.motors[1].speed = -40
            elif angle < 10 and angle > -10:
                R3.motors[0].speed = 50
                R3.motors[1].speed = 50
        else:
            R3.motors[0].speed = -100
            R3.motors[1].speed = 100

a = Arena()
populate_walls(7, 7)
for i in xrange(40, NUMBER_OF_TOKENS+40):
    token_list.append(Token(i))

robotlist = []
R0 = Robot(0)
R1 = Robot(1)
R2 = Robot(2)
R3 = Robot(3)

robotlist.append(R0)
robotlist.append(R1)
robotlist.append(R2)
robotlist.append(R3)

thread.start_new_thread(usercode0, ())
thread.start_new_thread(usercode1, ())
thread.start_new_thread(usercode2, ())
thread.start_new_thread(usercode3, ())

while True:
    n = 2
    for i in range(n):
        # Simulation step
        world.step(dt/n)
    for robot in robotlist:
        robot.update()
    for token in token_list:
        token.update()
    rate(RATE)
