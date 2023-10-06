import random
import operator
from job import *

# print out all values
# for j in jobs:
#     print(j.arrival_time, j.service_time, j.priority)

# graph(jobs)

# non pre-emptive

# using Python 3.11.5
# Seeds are:
# 139342
# 761639
# 567317
# 292160
# 803931

seeds = [139342, 761639, 567317, 292160, 803931]

# for s in seeds:
#     size = 20
#     jobs = [0] * size
#     seed = s

#     create_job(jobs, size, seed)
#     graph(jobs)

# # non-preemptive highest priority first, we get to look into the future

def hpf(jobs):
    # sort jobs into their priorities, and order 
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
    


size = 20
jobs = [0] * size
seed = 139342

create_job(jobs, size, seed)
jobs = hpf(jobs)
graph(jobs)
