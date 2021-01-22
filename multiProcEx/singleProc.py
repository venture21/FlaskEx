import time

def count(name):
    for i in range(1,50001):
        print(name,":",i)

# p1~p4까지 각각 1~50000까지를 출력한다.
if __name__ == "__main__":
    startTime = time.time()
    num_list = ['p1', 'p2', 'p3', 'p4']
    for num in num_list:
        count(num)

    endTime   = time.time()
    print("execute time : %s " %(endTime-startTime))

