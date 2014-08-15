
import threading
from visual import rate

from objects import Arena, Robot, Token, populate_walls
from variables import dt, NUMBER_OF_TOKENS, RATE, token_list, world

import registration

# TODO: make this a command line parameter?
import usercode

def swarmcode(number):
    while True:
        robot_list[number].motors[0].speed = -50.0
        robot_list[number].motors[1].speed = 50.0

a = Arena()
populate_walls(7, 7)
for i in xrange(40, NUMBER_OF_TOKENS+40):
    token_list.append(Token(i))

user_funcs = registration.get_user_funcs()

assert len(user_funcs) == 4, "Wrong number of user functions (got {0}).".format(len(user_funcs))

robot_threads = []
robotlist = []

for i, func in enumerate(user_funcs):
    robot = Robot(i)
    thread = threading.Thread(target=func, args=(robot,))
    robot_threads.append(thread)
    robotlist.append(robot)
    thread.start()

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
