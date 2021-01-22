# 아래의 코드는 리눅스와 유닉스의 구조에 의존성을 가지고 있는 코드이다.

import time
import logging

import os
import signal
import argparse

class Fruits:
    FRUITS_LIST = ["Apple","Watermelon","Orange","Strawberry","Grape","Cherry","Mango", "Nectarine","Banana"]

    def __init__(self, log_file=None):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger("Fruits_List")
        self.log_file = log_file

        if log_file:
            self.log_handler = logging.FileHandler(self.log_file)
            self.logger.addHandler(self.log_handler)

        self.__stop = False

        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)


    def main(self):
        i = 0
        self.logger.info("Start Fruits, PID {0}".format(os.getpid()))

        while not self.__stop:
            self.logger.info(self.FRUITS_LIST[i % len(self.FRUITS_LIST)])
            i += 1
            time.sleep(1)


    def stop(self, signum, frame):
        self.__stop = True
        self.logger.info("Receive Signal {0}".format(signum))
        self.logger.info("Stop Fruits")
