from random import random
# oppgave 7
# del A
def find_pi(n):
    inside_cirkle = 0
    outside_cirkle = 0
    for i in range(n):
        random_x = random.random()
        random_y = random.random()
        random_x = ((random_x * 2) - 1)
        random_y = ((random_y * 2) - 1)
        d = (abs((random_x-0)**2)+((random_y-0)**2))**0.5
        if d < 1: inside_cirkle += 1
        else: outside_cirkle += 1
    return ((inside_cirkle/outside_cirkle)*4)
