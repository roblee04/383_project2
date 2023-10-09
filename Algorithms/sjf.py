from job import create_job
from prettytable import PrettyTable

# need prettytable module, set up virtual env and pip install
# $ python3 -m venv .venv
# $ source .venv/bin/activate
# $ pip install -U prettytable

size = 20
jobs = [0] * size
seeds = [139342, 761639, 567317, 292160, 803931]
total_avg_tat = 0
total_avg_wt = 0
total_avg_rt = 0
total_avg_throughput = 0
total_avg_completion_time = 0
for seed in seeds:
    create_job(jobs, size, seed)
    completed_jobs = list()
    time = 0
    avg_turn_around_time = 0
    avg_waiting_time = 0
    avg_response_time = 0
    table = PrettyTable()
    table.field_names = ["Process Name", "Arrival Time", "Burst Time", "Turn Around Time",
                         "Wait Time", "Response Time", "Completion Time"]

    while len(completed_jobs) < size:
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
            completed_jobs.append(job.id)
            table.add_row([job.id, job.arrival_time, job.service_time, time-job.arrival_time,
                           time-job.arrival_time-job.service_time, time-job.service_time-job.arrival_time, time])
        else:
            time += 1
    total_avg_tat += avg_turn_around_time/size
    total_avg_wt += avg_waiting_time/size
    total_avg_rt += avg_response_time/size
    total_avg_throughput += size/time
    total_avg_completion_time += time
    print("Job scheduling order: ", completed_jobs)
    print("Avg Turn around time: ", avg_turn_around_time/size)
    print("Avg Waiting time: ", avg_waiting_time/size)
    print("Avg Response time: ", avg_response_time/size)
    print("Throughput: ", size/time)
    print("Completion Time: ", time)
    print(table)
    print()

print("----------------------------------------------------------------------")
print("Average Statistics for 5 runs")
print("----------------------------------------------------------------------")

print("Turn around time: ", total_avg_tat/5)
print("Waiting time: ", total_avg_wt/5)
print("Response time: ", total_avg_rt/5)
print("Throughput: ", total_avg_throughput/5)
print("Completion time: ", total_avg_completion_time/5)
