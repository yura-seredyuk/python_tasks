
from multiprocessing import Pool
import time
import tracemalloc
from random import randint

# work = []
# for i in range(ord('A'), ord('Z')+1):
#     work.append([chr(i),randint(2,10)])
# print(work)

work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])

work = [['A', 8], ['B', 10], ['C', 7], ['D', 9], ['E', 8], ['F', 4], ['G', 7], ['H', 10], ['I', 8], ['J', 5], ['K', 9], ['L', 7], ['M', 7], ['N', 8], ['O', 2], ['P', 2], ['Q', 2], ['R', 9], ['S', 10], ['T', 7], ['U', 3], ['V', 9], ['W', 4], ['X', 4], ['Y', 10], ['Z', 9]]

def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])


def pool_handler():
    p = Pool()
    p.map(work_log, work)


if __name__ == '__main__':
    start = time.time()
    tracemalloc.start()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())

    pool_handler()
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())
    print("time: ", time.time() - start)

 


