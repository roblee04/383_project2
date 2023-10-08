import random
import operator
from job import *


def hpf(jobs): # 4 is the highest priority
    # first, sort by arrival time
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    for j in jobs:
        prio = j.priority

        if prio == 1:
            p1.append(j)
        elif prio == 2:
            p2.append(j)
        elif prio == 3:
            p3.append(j)
        else:
            p4.append(j)
    
    # jobs all in their priority queues, now sort by arrival time
    p1.sort(key=lambda x: x.arrival_time)
    p2.sort(key=lambda x: x.arrival_time)
    p3.sort(key=lambda x: x.arrival_time)
    p4.sort(key=lambda x: x.arrival_time)

    # need to fill in the gaps. with runtime
    new_jobs = p1 + p2 + p3 + p4
    return new_jobs


seeds = [139342, 761639, 567317, 292160, 803931]

size = 20
jobs = [0] * size
seed = 139342

create_job(jobs, size, seed)

jobs = hpf(jobs)
graph(jobs)

# # iterate on all seeds
# for s in seeds:
#     size = 20
#     jobs = [0] * size
#     seed = s

#     create_job(jobs, size, seed)
    
#     startend = [] # startend, is a list used to help calculate all the outputs
#     jobs = hpf(jobs, startend)
#     print()
#     print("SEED: " + str(seed))
#     output(startend)

#     print("_________________________________________________")




