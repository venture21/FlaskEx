from multiprocessing import Process, current_process


def worker1(start, end):
    name = current_process().name
    print('{} : {}'.format(name, 'Starting'))
    print('arg1: {}, arg2 : {}'.format(start, end))
    #time.sleep(2)
    print('{} : {}'.format(name, 'Exiting'))


def worker2():
    name = current_process().name
    print('{} : {}'.format(name, 'Starting'))
    #time.sleep(2)
    print('{} : {}'.format(name, 'Exiting'))


if __name__ == '__main__':
    start = 1
    end   = 1000000
    worker_1 = Process(name='worker1', target=worker1, args=(start, end))
    worker_2 = Process(target=worker2)

    # process를 생성한 순서가 아닌 .start한 순서대로 시작된다.
    worker_2.start()
    worker_1.start()
