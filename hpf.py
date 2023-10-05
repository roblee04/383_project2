import random

class job:
    def __init__(self, arrival_time, service_time, priority):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority
        self.next = None # omit this if not using LL

def create_job(jobs, size, seed):

    random.seed(seed)

    for i in range(size):
        arrival_time = random.randint(0, 99)
        service_time = random.randint(1, 10)
        priority = random.randint(1, 4)

        new_job = job(arrival_time, service_time, priority)
        jobs[i] = new_job

def graph(jobs):
    a = ""
    for i in range(99):
        if (i / 10) in range(10):
            a += str(int((i / 10)))
        else:
            a += "-"

    a += "end"

    print(a, len(a))

    for j in jobs:

        a = ""
        for i in range(j.arrival_time):
            a += " "
        for i in range(j.service_time):
            a += "_"
        print(a + "\n")

# parameters
# size = 10
# jobs = [0] * size
# seed = 675824

# create_job(jobs, size, seed)

# print out all values
# for j in jobs:
#     print(j.arrival_time, j.service_time, j.priority)

# graph(jobs)

# non pre-emptive

# using Python 3.11.5
# Seeds are:
# 139342
# 761639
# 567317
# 292160
# 803931

l = [139342, 761639, 567317, 292160, 803931]

for s in l:
    size = 20
    jobs = [0] * size
    seed = s

    create_job(jobs, size, seed)
    graph(jobs)


