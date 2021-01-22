import time
from multiprocessing import Pool

def count(name):
    for i in range(1,1000001):
        print(name,":",i)

# p1~p4까지 각각 1~1000001까지를 출력한다.
if __name__ == "__main__":
    pool = Pool(processes=4)
    startTime = time.time()
    num_list = ['p1', 'p2', 'p3', 'p4']

    # single-process
    #for num in num_list:
    #    count(num)

    # multi-process
    pool.map(count, num_list)
    pool.close()
    pool.join()

    endTime   = time.time()
    print("execute time : %s " %(endTime-startTime))