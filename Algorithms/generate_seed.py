import random
import time
from job import *

# generate_seed.py is used to generate x amount of seeds for jobs

# logic:
# generate jobs and put into interval form --> [arrival time, arrival time + service time]
# check the FREE intervals of cpu time aka times not taken by jobs intervals, 
# make sure that they are all less than 2 quanta

# you can also graphically see this by calling graph() method, it is also a sanity check

# repeat until you want to find x amount of seeds
# you can also change the number of jobs per seed, recommended >= 20 jobs

# find a job seq so cpu not idle for more than 2 consecutive quanta
def findFreeinterval(arr, N):
    if N < 1:
        return
    P = []
    arr.sort(key = lambda a:a[0])
    for i in range(1, N):
        prevEnd = arr[i - 1][1]
        currStart = arr[i][0]
        if prevEnd < currStart:
            P.append([prevEnd, currStart])
    a = []
    for i in P:
        a.append(i)
    return a

# parameters
def find_seed(s):
    size = s
    jobs = [0] * size
    seed = int((time.time() % 1) * 1000000) # convert to better looking number
    # seed = time.time()

    create_job(jobs, size, seed)

    arr = []
    for j in jobs:
        arr.append([j.arrival_time, j.arrival_time + j.service_time])
        
    # Function call
    arr.append([0, 0]) # lower bound
    arr.append([99, 99]) # upper bound

    intervals = findFreeinterval(arr, len(arr))

    # check if all intervals >= 2, not greater than 2
    valid = True
    for i in intervals:
        s = i[0]
        e = i[1]

        if (e - s) > 2:
            valid = valid and False
        else:
            valid = valid and True

    return [valid, seed, jobs]
        

counter = 0
while counter != 5:
    valid, seed, jobs = find_seed(20)

    if valid:
        counter += 1
        print(seed)
        graph(jobs)

