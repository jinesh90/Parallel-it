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
QUEUE_SIZE = 10

# Explicitly define LIFO Queue
Queue = queue.LifoQueue()
for i in range(QUEUE_SIZE):
    Queue.put(i)

print("Age Queue Populated")



threads = []

for i in range(MAX_THREADS):
    thread = threading.Thread(target=consumer, args=(Queue,))
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()

"""
OUT PUT will be
<Thread(Thread-1, started 140388729362176)> removed 9 from the queue
<Thread(Thread-2, started 140388720969472)> removed 8 from the queue
<Thread(Thread-3, started 140388712576768)> removed 7 from the queue
<Thread(Thread-1, started 140388729362176)> removed 6 from the queue
<Thread(Thread-2, started 140388720969472)> removed 5 from the queue
<Thread(Thread-3, started 140388712576768)> removed 4 from the queue
<Thread(Thread-1, started 140388729362176)> removed 3 from the queue
<Thread(Thread-2, started 140388720969472)> removed 2 from the queue
<Thread(Thread-3, started 140388712576768)> removed 1 from the queue
<Thread(Thread-1, started 140388729362176)> removed 0 from the queue

"""