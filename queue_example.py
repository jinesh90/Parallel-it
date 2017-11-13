"""
Demo thread safe Queue Object, This object available in python 3.0
"""
import threading
import queue
import random
import time


def consumer(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            print("Nothing comes out from queue")
            break
        print("{} removed {} from the queue".format(threading.current_thread(),item))
        queue.task_done()
        time.sleep(1)


MAX_THREADS = 3
QUEUE_SIZE = 30
Queue = queue.Queue()

for i in range(QUEUE_SIZE):
    Queue.put(random.randint(18,92))

print("Age Queue Populated")

threads = []

for i in range(MAX_THREADS):
    thread = threading.Thread(target=consumer, args=(Queue,))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()