import multiprocessing

def worker():
    """worker function"""
    print 2**1048576
    return

if __name__ == '__main__':
    jobs = []
    cpu = multiprocessing.cpu_count()
    for i in range(cpu):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()

