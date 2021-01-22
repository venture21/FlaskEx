from multiprocessing import Process, current_process
import time
import sys

def daemon():
    print('Starting:', current_process().name)
    time.sleep(2)
    print('Exiting :', current_process().name)

def non_daemon():
    print('Starting:', current_process().name)
    print('Exiting :', current_process().name)

if __name__ == '__main__':
    d = Process(name='daemon', target=daemon)
    d.daemon = True

    n = Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
    print('program exit')