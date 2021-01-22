import time
import logging

class Fruits:
    FRUITS_LIST = ["Apple","Watermelon","Orange","Strawberry","Grape","Cherry","Mango", "Nectarine","Banana"]

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("Fruits_List")

    def main(self):
        i = 0
        while True:
            self.logger.info(self.FRUITS_LIST[i % len(self.FRUITS_LIST)])
            i += 1
            time.sleep(1)

myFruits = Fruits()
myFruits.main()