def hpf(jobs): # 4 is the highest priority
    # first, sort by arrival time
    p1 = []
    p2 = []
    p3 = []
    p4 = []

    for j in jobs:
        prio = j.priority

        if prio == 1:
            p1.append(j)
        elif prio == 2:
            p2.append(j)
        elif prio == 3:
            p3.append(j)
        else:
            p4.append(j)
    
    # jobs all in their priority queues, now sort by arrival time
    p1.sort(key=lambda x: x.arrival_time)
    p2.sort(key=lambda x: x.arrival_time)
    p3.sort(key=lambda x: x.arrival_time)
    p4.sort(key=lambda x: x.arrival_time)

    # need to fill in the gaps. with runtime
    new_jobs = p1 + p2 + p3 + p4
    return new_jobs