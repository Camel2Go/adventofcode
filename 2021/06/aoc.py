#!/bin/python

# ======== setup ===========
import sys
data = [int(x) for x in open(sys.path[0]+"/data").read().split(',')]

# ======== code =======

def simulate(state, days):
    for _ in range(days):
        new = state[0]
        state = state[1:]
        state[6] += new
        state.append(new)
    return state

state = []
for i in range(9):
    state.append(data.count(i))

print(sum(simulate(state, 80)))
print(sum(simulate(state, 256)))