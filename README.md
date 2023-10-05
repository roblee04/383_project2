
# 383_project2

# Process Scheduling Algorithms

This assignment will give you experience with process scheduling algorithms.
Write a Java or C program that performs runs of the following process scheduling algorithms:

- First-come first-served (FCFS) [non-preemptive]
- Shortest job first (SJF) [non-preemptive]
- Shortest remaining time (SRT) [preemptive]
- Round robin (RR) [preemptive]
- Highest priority first (HPF) [both non-preemptive and preemptive]

Run each algorithm for 100 quanta (time slices), labeled 0 through 99. Before each run, generate a set of simulated processes. For each simulated process, randomly generate:
- An arrival time: a float value from 0 through 99 (measured in quanta).
- An expected total run time: a float value from 0.1 through 10 quanta.
- A priority: integer 1, 2, 3, or 4 (1 is highest)


# Outputs for each algorithm run (total 30 runs)
- Each created process’s name (such as A, B, C, ...), arrival time, expected run time, and priority. 
- A time chart of the 100+ quanta, such as ABCDABCD ...

Show a process’s name in a quantum even if it completed execution before the end of that quantum (so then the CPU is idle at least until the start of the next quantum).

- Calculated statistics for the processes during the run:
  - Average turnaround time
  - Average waiting time
  - Average response time
- Calculated statistic for the algorithm for the run:
  - Throughput
