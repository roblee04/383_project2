from job import create_job, graph
from collections import deque

# Parameters
l = [139342, 761639, 567317, 292160, 803931]
quantum = 1

for s in l:
    size = 20
    jobs = [0] * size
    seed = s

    create_job(jobs, size, seed)
    
    # Graphing and Printing job details
    graph(jobs)

    for job in jobs:
        print(f"ID: {job.id}, Arrival Time: {job.arrival_time}, Service Time: {job.service_time}, Priority: {job.priority}")

    # Initialize time & job variables
    time = 0
    avg_turnaround_time = 0
    avg_response_time = 0
    avg_wait_time = 0  

    job_queue = deque()
    started_jobs = set()
    completed_jobs = []

    # Sort jobs by arrival time
    jobs.sort(key=lambda x: x.arrival_time)

    # Perform Round Robin scheduling
    print("Simulation Start:")
    while jobs or job_queue:
        print(f"Time: {time}")
        # Add jobs to the queue when their arrival time has been reached
        while jobs and jobs[0].arrival_time <= time:
            print(f"Job {jobs[0].id} arrived at {time}")
            job_queue.append(jobs.pop(0))

        if not job_queue:
            # No jobs are ready, so we can't proceed.
            time += quantum
            continue

        current_job = job_queue.popleft()

        # Track response time
        if current_job not in started_jobs:
            started_jobs.add(current_job)
            avg_response_time += time - current_job.arrival_time  

        if current_job.service_time > quantum:
            print(f"Job {current_job.id} worked for {quantum}")
            time += quantum
            avg_wait_time += quantum * len(job_queue)
            current_job.service_time -= quantum          
            job_queue.append(current_job)
        else:
            print(f"Job {current_job.id} completed!")
            time += current_job.service_time
            avg_wait_time += current_job.service_time * len(job_queue)
            current_job.service_time = 0
            completed_jobs.append((current_job, time))

    # Print each job completion times in order and add them to the overall turnaround time
    for job, completion_time in completed_jobs:
        print(f"Job {job.id} completed at time {completion_time}")
        avg_turnaround_time += completion_time - job.arrival_time

    # Calculate and print average turnaround time, average waiting time, and average response time
    num_jobs = len(completed_jobs)
    print(f"Number of jobs = {num_jobs}")   
    avg_turnaround_time /= num_jobs
    avg_response_time /= num_jobs
    avg_wait_time /= num_jobs

    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Response Time: {avg_response_time:.2f}")
    print(f"Average Wait Time: {avg_wait_time:.2f}")

    # Calculate and print throughput
    throughput = len(completed_jobs)/time
    print(f"Throughput: {throughput:.2f} jobs per quantum\n")