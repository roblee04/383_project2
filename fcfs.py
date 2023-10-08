from job import create_job, graph

def fcfs_scheduling(jobs):
    time = 0  # Current time
    completed_jobs = []  # List to store completed jobs

    for job in jobs:
        if time < job.arrival_time:
            time = job.arrival_time  # Wait for the job to arrive if necessary
        job.start_time = time
        job.completion_time = time + job.service_time
        job.turnaround_time = job.completion_time - job.arrival_time
        job.waiting_time = job.turnaround_time - job.service_time
        time = job.completion_time
        completed_jobs.append(job)

    return completed_jobs

def main():
    # Parameters
    size = 10
    jobs = [0] * size
    # seed = 42069
    seeds = [139342, 761639, 567317, 292160, 803931] 

    total_avg_turnaround_time = 0
    total_avg_waiting_time = 0
    total_avg_response_time = 0
    total_throughput = 0

    for seed in seeds:
        total_turnaround_time = 0
        total_waiting_time = 0 
        total_response_time  = 0        

        # Generate random jobs
        create_job(jobs, size, seed)

        # Perform FCFS scheduling
        completed_jobs = fcfs_scheduling(jobs)

        # Calculate the total time it took for all processes to complete
        total_completion_time = max(job.completion_time for job in completed_jobs)

        # Print out job details and scheduling results
        print("Job\tArrival Time\tService Time\tCompletion Time\tTurnaround Time\tWaiting Time")
        for job in completed_jobs:
            print(
                f"{job.id}\t{job.arrival_time}\t\t{job.service_time}\t\t{job.completion_time}\t\t{job.turnaround_time}\t\t{job.waiting_time}"
            )
            total_turnaround_time += job.turnaround_time
            total_waiting_time += job.waiting_time
            total_response_time += (job.start_time - job.arrival_time)


        # Print statistics
        avg_turnaround_time = total_turnaround_time / size
        avg_waiting_time = total_waiting_time / size
        avg_response_time = total_response_time / size

        throughput = size/total_completion_time

        print("\nStatistics:")
        print(f"Average Turnaround Time: {avg_turnaround_time}")
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average Response Time: {avg_response_time}")
        print(f"Throughput: {throughput} processes per quantum")  

        total_avg_turnaround_time += avg_turnaround_time
        total_avg_waiting_time += avg_waiting_time
        total_avg_response_time += avg_response_time
        total_throughput += throughput

    
    # --------------- Print avg statistics of 5 runs ----------------

    print("\nAverage Statistics of 5 runs :")
    print(f"Average Turnaround Time: {total_avg_turnaround_time/5}")
    print(f"Average Waiting Time: {total_avg_waiting_time/5}")
    print(f"Average Response Time: {total_avg_response_time/5}")
    print(f"Throughput: {total_throughput/5} processes per quantum")  




if __name__ == '__main__':
    main()
