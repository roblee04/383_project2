from job import *
from collections import deque

def output(lst):
    # Each created process’s name (such as A, B, C, ...), arrival time, expected runtime, and priority.
    print("PROCESS INFORMATION:")
    print("pid: |" + "arr:  |" + "end: |" + "prio: ")

    for j in lst:
        b = ""
        b += "   " + j.id + " |"
        b += "   " + str(j.start) + " |"
        b += "   " + str(j.end) + " |"
        b += "   " + str(j.priority) + " |"
        
        print(b)  
    print("Total Jobs Run: " + str(len(lst)))
    print()

    # Statistics
    count = 0
    tot_tat = 0
    tot_wait = 0
    tot_res = 0

    for j in lst: 
        # Average turnaround time, Turnaround Time = Completion Time – Arrival Time
        tat = j.end - j.arrival_time
        # Average waiting time, Waiting Time = TAT - Service Time
        wait = tat - j.service_time
        # Average response time, Response Time = Run Time – Arrival Time
        res = j.start - j.arrival_time

        tot_tat += tat
        tot_wait += wait
        tot_res += res
        count += 1
    
    print("STATISTICS: ")
    print("Average turnaround time: " + str(round(tot_tat / count, 2)))
    print("Average waiting time: " + str(round(tot_wait / count, 2)))
    print("Average response time: " + str(round(tot_res / count, 2)))
    # Throughput = Jobs Completed / Total Time Ran 
    print("Throughput: " + str(round((count / lst[-1].end), 2)))

def rr(jobs):
    time = 0    # global time
    tc = ""     # time chart
    job_queue = deque()
    completed_jobs = []

    # Sort jobs by arrival time
    jobs.sort(key=lambda x: x.arrival_time)

    # print("Simulation Start:")
    while time <= 99 or job_queue:
        # print(f"Time: {time}")
        # Add jobs to the queue when their arrival time has been reached
        while time <= 99 and jobs and jobs[0].arrival_time == time:
            # print(f"Job {jobs[0].id} arrived at {time}")
            job_queue.append(jobs.pop(0))

        if not job_queue:
            # No jobs are ready, so we can't proceed.
            time += 1
            tc += '-'
            continue

        curr_job = job_queue.popleft()

        # Track start time
        if curr_job.time_on_cpu == 0:
            # print(f"Job {curr_job.id} arrived at {time}")
            curr_job.start = time
            # Make sure no jobs start running after time = 99
            if time > 99:
                while job_queue and curr_job.time_on_cpu == 0:
                    curr_job = job_queue.popleft()
            # If final job hasn't started yet, will execute if statement below
            if curr_job.start > 99:
                break
            # print(f"Job {curr_job.id} arrived at {time}")
                  
        curr_job.time_on_cpu += 1
        tc += curr_job.id

        if curr_job.time_on_cpu == curr_job.service_time:  
            # Check if the job's start time is within the time limit
            # print(f"Job {curr_job.id} completed at {time}")
            curr_job.end = time
            completed_jobs.append(curr_job)
        else:   
            job_queue.append(curr_job)
        
        time += 1
    
    print("TIMECHART: \n" + tc + "\n")
    output(completed_jobs)


seeds = [139342, 761639, 567317, 292160, 803931]

for s in seeds:
    size = 20
    jobs = [0] * size
    seed = s

    create_job(jobs, size, seed)

    print()
    print("SEED: " + str(seed) + "\n")
    rr(jobs)

    print("_________________________________________________")