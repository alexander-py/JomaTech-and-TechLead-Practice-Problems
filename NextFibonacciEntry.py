from math import *


# the ratio of any two consecutive entries
# in the Fibonacci sequence
# rapidly approaches x=(1+sqrt5)/2.
# So if you multiply your number by (1+sqrt5)/2
# and round it to the nearest integer,
# you will get the next entry


def next_entry(lst):
    nextEntry = (1+sqrt(5))/2.0

    return [round(number * nextEntry) for number in lst]

test_integers =[]

print(next_entry(test_integers))

#input [89, 233, 377, 987]
#output [144, 377, 610, 1597]
#input [1,22,8]
#output [2, 36, 13]
