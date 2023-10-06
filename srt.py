from prettytable import PrettyTable
from job import create_job

class Job:
    def _init_(self, id, arrival_time, service_time, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority

def srtf_scheduler(jobs):
    current_time = 0
    completed_jobs = []
    avg_turnaround_time = 0
    avg_waiting_time = 0
    avg_response_time = 0

    # Create a PrettyTable to store the output table
    table = PrettyTable()
    table.field_names = ["Process Name", "Arrival Time", "Start Time", "End Time", "Run Time",
                         "Response Time", "Wait Time", "Turn Around Time", "Priority"]

    while jobs:
        runnable_jobs = [job for job in jobs if job.arrival_time <= current_time]

        if runnable_jobs:
            shortest_job = min(runnable_jobs, key=lambda job: job.service_time)
            shortest_job.service_time -= 1
            current_time += 1

            if shortest_job.service_time == 0:
                jobs.remove(shortest_job)
                completed_jobs.append(shortest_job)

                # Calculate Run Time, Response Time, Wait Time, and TurnAround Time
                start_time = current_time - 1
                end_time = current_time

                response_time = start_time - shortest_job.arrival_time
                wait_time = response_time - shortest_job.service_time
                turnaround_time = end_time - shortest_job.arrival_time

                # Add job details to the PrettyTable
                table.add_row([shortest_job.id, shortest_job.arrival_time, start_time, end_time,
                               end_time - start_time, response_time, wait_time, turnaround_time, shortest_job.priority])

                # Update averages
                avg_turnaround_time += turnaround_time
                avg_waiting_time += wait_time
                avg_response_time += response_time
        else:
            current_time += 1

    print(table)

    return completed_jobs, avg_turnaround_time, avg_waiting_time, avg_response_time

if __name__ == '__main__':
    # Create jobs using your existing create_job function
    size = 20
    jobs = [0] * size
    seed = 42069

    create_job(jobs, size, seed)

    # Sort jobs by arrival time and priority for SRTF
    jobs.sort(key=lambda job: (job.arrival_time, job.priority))

    completed_jobs, avg_turnaround_time, avg_waiting_time, avg_response_time = srtf_scheduler(jobs)

    for job in completed_jobs:
        print(f"Job {job.id} completed.")

    print("Avg TRT:", avg_turnaround_time / size)
    print("Avg WT:", avg_waiting_time / size)
    print("Avg RT:", avg_response_time / size)