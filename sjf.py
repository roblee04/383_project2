from job import create_job

jobs = [0] * 10
size = 10
seeds = [42069]
for seed in seeds:
    create_job(jobs, size, seed)

    completed_jobs = set()
    time = 1
    avg_turn_around_time = 0
    avg_waiting_time = 0
    avg_response_time = 0

    while time < 100 and len(completed_jobs) < size:
        job_queue = []
        for job in jobs:
            if job.arrival_time <= time and job.id not in completed_jobs:
                job_queue.append(job)
        if job_queue:
            job_queue.sort(key=lambda x: x.service_time)
            job = job_queue[0]
            avg_waiting_time += time-job.arrival_time
            avg_response_time += time-job.arrival_time
            time += job.service_time
            avg_turn_around_time += time-job.arrival_time
            completed_jobs.add(job.id)
        else:
            time += 1

    print("Avg TAT: ", avg_turn_around_time/10)
    print("Avg WT: ", avg_waiting_time/10)
    print("Avg RT: ", avg_response_time/10)
