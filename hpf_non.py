import random
import operator
from job import *


# using Python 3.11.5
# Seeds are:
# 139342
# 761639
# 567317
# 292160
# 803931


# # non-preemptive highest priority first, we get to look into the future


def output(lst):

    # Each created process’s name (such as A, B, C, ...), arrival time, expected runtime, and priority.
    print("PROCESS INFORMATION:")
    print("pid: |" + "arr:  |" + "run: |" + "prio: ")

    for j in lst:
        b = ""
        b += "   " + j[0] + " |"
        b += "   " + str(j[2]) + " |"
        b += "   " + str(j[3]) + " |"
        b += "   " + str(j[1]) + " |"
        # uncomment block for graphical view
        # print("pid: " + j[0] + " prio: " + str(j[1]) + " start: " + str(j[2]) + " end: " + str(j[3]))
        # c = ""
        # c += "pid: " + j[0] + " prio: " + str(j[1]) + " |"

        # for i in range(j[2]):
        #     c += " "
        # for i in range(j[3] - j[2]):
        #     c += "_"
        # print(c )
        
        print(b)  
    print("total jobs: " + str(len(lst)))
    print()

    # Time chart
    print("TIME CHART: " )
    tc = ""
    for j in lst:
        c = j[0]
        for i in range(j[3]-j[2]):
            tc += c
    
    print(tc + "\n" + "total cpu time used: " + str(len(tc)) + "\n")

    # Statistics

    count = 0
    tot_tat = 0
    tot_wait = 0
    tot_res = 0
    for j in lst:
        # lst element: [id, prio, start, end, arrival_time, service time]
        
        # Average turnaround time, Turnaround Time = Completion Time – Arrival Time
        tat = j[3] - j[4]
        # Average waiting time, Waiting Time = TAT - Service Time
        wait = tat - j[5] 
        # Average response time, Response Time = Start Time – Arrival Time
        res = j[2] - j[4]

        tot_tat += tat
        tot_wait += wait
        tot_res += res
        count += 1
    
    print("STATISTICS: ")
    print("Average turnaround time: " + str(tot_tat / count))
    print("Average waiting time: " + str(tot_wait / count))
    print("Average response time: " + str(tot_res / count))
    print()
    
    # throughput = # jobs completed in 99 time slices, truncate last job
    count = 0
    for j in lst:
        if j[3] > 99:
            break
        count += 1

    print("Throughput (jobs completed in 99 time slices): " + str(count))


def hpf(jobs, lst): # 4 is the highest priority
    # first, sort by arrival time
    jobs.sort(key=lambda x: x.arrival_time)

    # second, add first jobs to working q, will use a python list for simplification
    working_q = []
    time = 0       # global time
    time_left = 0 # time left to finish current job, 

    job_order = []
    num_jobs = len(jobs)
    while working_q or num_jobs > 0:
        # add jobs to the working q who have arrived at time slice x
        
        for j in jobs:  # pretty sure there is a problem if removing more than 2 jobs
            if j.arrival_time == time:
                working_q.append(j)
                num_jobs -= 1
        
        # on each iteration, sort working queue by priority
        working_q.sort(key=lambda x: x.priority, reverse = True)
        # this may starve other processes, can implement aging here

        # # put a new job to work
        if time_left == 0 and working_q:
            curr_job = working_q.pop(0)
            id = curr_job.id
            time_left += curr_job.service_time
            job_order.append(curr_job)

            # print out scheduled time and est end time
            start = time
            end = time + curr_job.service_time
            lst.append([id, curr_job.priority, start, end, curr_job.arrival_time, curr_job.service_time])

        # increment time 
        time += 1
        # decrement time_left if there is a job running
        if time_left > 0:
            time_left -= 1
    
    return job_order


seeds = [139342, 761639, 567317, 292160, 803931]

# iterate on all seeds
for s in seeds:
    size = 20
    jobs = [0] * size
    seed = s

    create_job(jobs, size, seed)
    
    startend = [] # startend, is a list used to help calculate all the outputs
    jobs = hpf(jobs, startend)
    print()
    print("SEED: " + str(seed))
    output(startend)

    print("_________________________________________________")




