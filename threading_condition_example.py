"""
This example demo how to use Condition for thread synchronization in python.typical consumer-producer type problem will
be solved by this.condition is useful when you want to synchronize input/output,Example. one end of network is fast and
other end it slow, Typical LAN-WAN scenario, In this Example we have two consumer who are fast and producer is producing
data at slow rate( we explicitly put 3 second delay)
"""

import threading
import time
import random

# this class produce random integer and notify to peer thread class


class Producer(threading.Thread):

    def __init__(self, prod_list, produce, condition):
        self.condition = condition
        self.prod_list = prod_list
        self.produce = produce
        threading.Thread.__init__(self)

    def run(self):
        # Run forever
        while True:
            produce = random.choice(self.produce)
            # condition acquired
            self.condition.acquire()
            print("Condition acquired by producer: {}".format(self.name))
            print("Product made by producer: {}".format(produce))
            self.prod_list.append(produce)

            # notify to another thread(consumer) thread that i am ready with product
            self.condition.notify()
            # release condition after notification, so peer thread can access
            print("Condition released by producer: {}".format(self.name))
            self.condition.release()
            print("***********Status of production line is*********** : {}".format(self.prod_list))
            time.sleep(1)

# Define Consumer thread


class Consumer(threading.Thread):

    def __init__(self, prod_list, condition, timeout=None):
        self.prod_list = prod_list
        self.condition = condition
        self.timeout = timeout
        threading.Thread.__init__(self)

    def run(self):
        while True:
            # acquire condition
            self.condition.acquire()
            print("Condition acquired by consumer :{}".format(self.name))
            while True:
                if self.prod_list:
                    produce = self.prod_list.pop()
                    print("produce {} poped by consumer {}".format(produce, self.name))
                    break
                print("Condition wait by consumer: {}".format(self.name))
                self.condition.wait(timeout=self.timeout)
            print("Consumer releasing condition {}".format(self.name))
            self.condition.release()


def main():
    produce = ["tomato", "potato", "eggplant", "eggs", "lentils", "cauliflower", "orange", "apple", "banana"]
    prod_list = []
    condition = threading.Condition()

    # Producer
    producer1 = Producer(prod_list, produce, condition)

    # start producer to produce some product
    producer1.start()

    # Define consumer
    consumer1 = Consumer(prod_list, condition)
    consumer2 = Consumer(prod_list, condition)
    consumer1.start()
    consumer2.start()


    # join threads
    producer1.join()
    consumer1.join()
    consumer2.join()


main()
