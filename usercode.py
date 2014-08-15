"Usercode Functions"

import time

from registration import usercode

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


@usercode("team-0")
def usercode0(R0):
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

@usercode("team-1")
def usercode1(R1):
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

@usercode("team-2")
def usercode2(R2):
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

@usercode("team-3")
def usercode3(R3):
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
