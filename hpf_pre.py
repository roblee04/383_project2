import random
import operator
from job import *

def output(lst):

    # Each created process’s name (such as A, B, C, ...), arrival time, expected runtime, and priority.
    print("PROCESS INFORMATION:")
    print("pid: |" + "arr:  |" + "run: |" + "prio: ")

    for j in lst:
        b = ""
        b += "   " + j.id + " |"
        b += "   " + str(j.start) + " |"
        b += "   " + str(j.end) + " |"
        b += "   " + str(j.priority) + " |"
        
        print(b)  
    print("total jobs: " + str(len(lst)))
    print()

    # Statistics

    count = 0
    tot_tat = 0
    tot_wait = 0
    tot_res = 0
    for j in lst:
        # lst element: [id, prio, start, end, arrival_time, service time]
        
        # Average turnaround time, Turnaround Time = Completion Time – Arrival Time
        tat = j.end - j.start
        # Average waiting time, Waiting Time = TAT - Service Time
        wait = tat - j.service_time
        # Average response time, Response Time = Run Time – Arrival Time
        res = j.end - j.arrival_time

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
        if j.end > 99:
            break
        count += 1

    print("Throughput (jobs completed in 99 time slices): " + str(count))

def hpf(jobs): # 4 is the highest priority
    # 4 priority queues, trickle down when there are free time slices
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    tc = ""

    time = 0       # global time
    time_left = 0 # time left to finish current job, 

    job_order = []
    num_jobs = len(jobs)
    while p1 or p2 or p3 or p4 or num_jobs > 0:
        # add jobs to the working q who have arrived at time slice x
        
        for j in jobs: 
            if j.arrival_time == time:
                # if we find jobs at the time slice, add the job
                prio = j.priority
                if prio == 1:
                    p1.append(j)
                elif prio == 2:
                    p2.append(j)
                elif prio == 3:
                    p3.append(j)
                else:
                    p4.append(j)
                # decrement jobs left to add
                num_jobs -= 1

        # a = len(p1) + len(p2) + len(p3) + len(p4)
        # print(a, num_jobs)

        # temp vars for later
        curr_job = None
        id = "0"

        # for each time slice, work on the highest priority job
        # trickle down in priority queues
        if p4:
            curr_job = p4[0]
            id = curr_job.id
            curr_job.time_on_cpu += 1

            if curr_job.start == 0:
                curr_job.start = time

            # if we worked on job enough, it is popped
            if curr_job.time_on_cpu == curr_job.service_time:
                job_order.append(p4.pop(0))

                curr_job.end = time

        elif p3:
            curr_job = p3[0]
            id = curr_job.id
            curr_job.time_on_cpu += 1

            if curr_job.start == 0:
                curr_job.start = time
            
            if curr_job.time_on_cpu == curr_job.service_time:
                job_order.append(p3.pop(0))

                curr_job.end = time

        elif p2:
            curr_job = p2[0]
            id = curr_job.id
            curr_job.time_on_cpu += 1

            if curr_job.start == 0:
                curr_job.start = time
            
            if curr_job.time_on_cpu == curr_job.service_time:
                job_order.append(p2.pop(0))

                curr_job.end = time

        elif p1:
            curr_job = p1[0]
            id = curr_job.id
            curr_job.time_on_cpu += 1
            
            if curr_job.start == 0:
                curr_job.start = time

            if curr_job.time_on_cpu == curr_job.service_time:
                job_order.append(p1.pop(0))

                curr_job.end = time

        if id != "0":
            tc += id

        
        #increment time
        time += 1

    print("TIMECHART: \n" + tc + "\n")

    output(job_order)

            
    return job_order


seeds = [139342, 761639, 567317, 292160, 803931]

# iterate on all seeds
for s in seeds:
    size = 20
    jobs = [0] * size
    seed = s

    create_job(jobs, size, seed)
    
    print()
    print("SEED: " + str(seed) + "\n")
    hpf(jobs)


    print("_________________________________________________")




