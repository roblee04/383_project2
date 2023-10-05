# 383_project2

Process Scheduling Algorithms
This assignment will give you experience with process scheduling algorithms.
Write a Java or C program that performs runs of the following process scheduling
algorithms:
• First-come first-served (FCFS) [non-preemptive]
• Shortest job first (SJF) [non-preemptive]
• Shortest remaining time (SRT) [preemptive]
• Round robin (RR) [preemptive]
• Highest priority first (HPF) [both non-preemptive and preemptive]
Run each algorithm for 100 quanta (time slices), labeled 0 through 99. Before each
run, generate a set of simulated processes. For each simulated process, randomly
generate:
• An arrival time: a float value from 0 through 99 (measured in quanta).
• An expected total run time: a float value from 0.1 through 10 quanta.
• A priority: integer 1, 2, 3, or 4 (1 is highest)
