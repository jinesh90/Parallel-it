"""
Lock is preventive strategy to avoid two threads to interfer each others task, here in this example
if users remove thread lock, program perhaps never complete as thread-1 is increasing value of global
variable and thread-2 decreasing value simultaneously,while user add lock, whoever ( thread-1, thread-2)
acquires lock first , finish task and release.
"""

import threading
import time
import random

# Global variable that shared between two threads
counter = 1

# Define Lock for thread locks
lock = threading.Lock()


# Thread method that increase global shared variable
def workerA():
    try:
        # Add lock for thread safe manner
        lock.acquire()
        global counter
        while counter < 1000:
            counter += 1
            print("Worker A is increasing argument variable to {}".format(counter))
            # put some random sleep for context switching , so other thread can execute
            sleep_time = random.randint(0, 1)
            time.sleep(sleep_time)
    finally:
        # finally release lock,
        lock.release()


# Thread method that decrease  global shared variable
def workerB():
    try:
        lock.acquire()
        global counter
        while counter > -1000:
            counter -= 1
            print("Worker B is decreasing argument variable to {}".format(counter))
            # put some random sleep for context switching , so other thread can execute
            sleep_time = random.randint(0, 1)
            time.sleep(sleep_time)
    finally:
        lock.release()


def main():
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print("Execution time {}".format(t1-t0))


main()


