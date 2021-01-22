#pip install multiprocess
import time
from multiprocessing import Process
import multiprocessing

def worker(num):
    """worker function"""
    print('Worker:{}'.format(num))
    time.sleep(10)
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

###################################################################
# 실행결과 : 추가로 5개의 프로세스가 생성되어 총 6개의 프로세스가 동작한다.
# $ ps -ef | grep multiProc0
###################################################################
#park     12772 12130  1 17:01 pts/1    00:00:00 /home/park/.conda/envs/pyExam/bin/python /home/park/PyExample/multiProc0.py
#park     12773 12772  0 17:01 pts/1    00:00:00 /home/park/.conda/envs/pyExam/bin/python /home/park/PyExample/multiProc0.py
#park     12774 12772  0 17:01 pts/1    00:00:00 /home/park/.conda/envs/pyExam/bin/python /home/park/PyExample/multiProc0.py
#park     12775 12772  0 17:01 pts/1    00:00:00 /home/park/.conda/envs/pyExam/bin/python /home/park/PyExample/multiProc0.py
#park     12776 12772  0 17:01 pts/1    00:00:00 /home/park/.conda/envs/pyExam/bin/python /home/park/PyExample/multiProc0.py
#park     12777 12772  0 17:01 pts/1    00:00:00 /home/park/.conda/envs/pyExam/bin/python /home/park/PyExample/multiProc0.py

