import random

class job:
    def __init__(self, id, arrival_time, service_time, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority
        self.age = 0    # needed for aging
        self.time_on_cpu = 0 # needed for preemptive hpf
        self.startend = [] # convenient to use to keep track of multiple start end times in preemptive hpf

def create_job(jobs, size, seed):

    random.seed(seed)

    start_id = 'A'
    id_counter = 0

    for i in range(size):
        id = chr(ord(start_id) + id_counter)
        id_counter += 1

        arrival_time = random.randint(0, 99)
        service_time = random.randint(1, 10)
        priority = random.randint(1, 4)

        new_job = job(id, arrival_time, service_time, priority)
        jobs[i] = new_job

# graphs your jobs / schedule, only accepts array
def graph(jobs):
    a = "pid| prio|"
    for i in range(99):
        if (i / 10) in range(10):
            a += str(int((i / 10)))
        else:
            a += "-"

    a += "end"

    print(a, len(a) - 13)

    for j in jobs:

        a = ""
        a += j.id + "  |  " + str(j.priority) + "  |"
        for i in range(j.arrival_time):
            a += " "
        for i in range(j.service_time):
            a += "_"

        print(a)
    print()


def main():
    # parameters
    size = 20
    jobs = [0] * size
    seed = 42069 

    create_job(jobs, size, seed)

    # print out all values

    for j in jobs:
        print(j.id, j.arrival_time, j.service_time, j.priority)

    #graph jobs
    graph(jobs)

# only execute main when you do python3 job.py
if __name__ == '__main__':
  main()