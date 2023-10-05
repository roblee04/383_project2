import random

class job:
    def __init__(self, arrival_time, service_time, priority, id):
        self.arrival_time = arrival_time
        self.service_time = service_time
        self.priority = priority
        self.id = id
        self.next = None # omit this if not using LL

def create_job(jobs, size, seed):

    random.seed(seed)

    for i in range(size):
        arrival_time = random.randint(0, 99)
        service_time = random.randint(1, 10)
        priority = random.randint(1, 4)

        new_job = job(arrival_time, service_time, priority, "P"+str(i))
        jobs[i] = new_job

# parameters
size = 10
jobs = [0] * size
seed = 42069

create_job(jobs, size, seed)

# print out all values
for j in jobs:
    print(j.arrival_time, j.service_time, j.priority, j.id)

