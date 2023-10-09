from prettytable import PrettyTable
from job import create_job

print("----------------------------------------------------------------------")
print("Output For Shortest Time First(SRT) Algorithm")
print("----------------------------------------------------------------------")
class Job:
    def __init__(self, id, arrival_time, burst_time, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.start_time = -1  # Initialize start time to -1

def main():
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

        # Convert job objects to the Job class used in this code
        job_list = [Job(j.id, j.arrival_time, j.service_time, j.priority) for j in jobs]

        time = 0
        completed_jobs = []
        avg_turnaround_time = 0
        avg_waiting_time = 0
        avg_response_time = 0
        table = PrettyTable()
        table.field_names = ["Process Name", "Arrival Time", "Burst Time", "Priority", "Turn Around Time",
                             "Wait Time", "Response Time", "Completion Time"]

        time_chart = []  # List to store the time chart

        while len(completed_jobs) < size:
            job_queue = [job for job in job_list if job.arrival_time <= time and job.id not in completed_jobs]

            if job_queue:
                job_queue.sort(key=lambda x: (x.remaining_time, -x.priority))
                job = job_queue[0]

                if job.start_time == -1:  # Check if job has not started yet
                    job.start_time = time

                time += 1
                job.remaining_time -= 1
                time_chart.append(job.id)  # Append the process name to the time chart

                if job.remaining_time == 0:
                    completed_jobs.append(job.id)
                    avg_turnaround_time += time - job.arrival_time
                    avg_waiting_time += time - job.arrival_time - job.burst_time
                    avg_response_time += job.start_time - job.arrival_time  # Calculate response time here
                    table.add_row([job.id, job.arrival_time, job.burst_time, job.priority, time - job.arrival_time,
                                   time - job.arrival_time - job.burst_time, job.start_time - job.arrival_time,
                                   time])
            else:
                time_chart.append("IDLE")
                time += 1

        total_avg_tat += avg_turnaround_time / size
        total_avg_wt += avg_waiting_time / size
        total_avg_rt += avg_response_time / size
        total_avg_throughput += size / time
        total_avg_completion_time += time

        # Print the time chart
        print("Time Chart:", " ".join(time_chart))

        print("Job scheduling order: ", completed_jobs)
        print("Avg Turn around time: ", avg_turnaround_time / size)
        print("Avg Waiting time: ", avg_waiting_time / size)
        print("Avg Response time: ", avg_response_time / size)
        print("Throughput: ", size / time, "processes per quantum time")
        print("Completion Time: ", time)
        print(table)
        print()

    print("----------------------------------------------------------------------")
    print("Average Statistics for 5 runs")
    print("----------------------------------------------------------------------")
    print("Turn around time: ", total_avg_tat / 5)
    print("Waiting time: ", total_avg_wt / 5)
    print("Response time: ", total_avg_rt / 5)
    print("Throughput: ", total_avg_throughput / 5, "processes per quantum time")
    print("Completion time: ", total_avg_completion_time / 5)

if __name__ == '__main__':
    main()
