import threading
import queue
import time


def consumer(queue):
    while not queue.empty():
        item = queue.get()
        if item is None:
            break
        print("{} removed {} from the queue".format(threading.current_thread(), item))
        queue.task_done()
        time.sleep(1)


Queue = queue.PriorityQueue()

# this items need to go as priority else they will not be in use.
food = ["apple", "ice-cream", "orange", "fish", "milk", "potato",
         "tomato", "onion", "meat", "banana", "yogurt", "butter",
         "chips","frozen-food", "soda", "beer"]
priority = ["4","0","4","2","0","5","5","5","3","2","1","1","5","1","3","3"]



items = list(zip(food, priority))


for i in range(len(items)):
    Queue.put((items[i][1],items[i][0]))
    print("Items :{} with priority {}".format(items[i][0],items[i][1]))


print("Item queue ready for pickup")

TOTAL_THREAD = 3
threads = []

for i in range(TOTAL_THREAD):
    t = threading.Thread(target=consumer, args=(Queue,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All items are empty")


"""
Output 
<Thread(Thread-1, started 139824414484224)> removed ('0', 'ice-cream') from the queue
<Thread(Thread-2, started 139824338040576)> removed ('0', 'milk') from the queue
<Thread(Thread-3, started 139824329647872)> removed ('1', 'butter') from the queue
<Thread(Thread-1, started 139824414484224)> removed ('1', 'frozen-food') from the queue
<Thread(Thread-3, started 139824329647872)> removed ('1', 'yogurt') from the queue
<Thread(Thread-2, started 139824338040576)> removed ('2', 'banana') from the queue
<Thread(Thread-1, started 139824414484224)> removed ('2', 'fish') from the queue
<Thread(Thread-3, started 139824329647872)> removed ('3', 'beer') from the queue
<Thread(Thread-2, started 139824338040576)> removed ('3', 'meat') from the queue
<Thread(Thread-3, started 139824329647872)> removed ('3', 'soda') from the queue
<Thread(Thread-1, started 139824414484224)> removed ('4', 'apple') from the queue
<Thread(Thread-2, started 139824338040576)> removed ('4', 'orange') from the queue
<Thread(Thread-3, started 139824329647872)> removed ('5', 'chips') from the queue
<Thread(Thread-2, started 139824338040576)> removed ('5', 'onion') from the queue
<Thread(Thread-1, started 139824414484224)> removed ('5', 'potato') from the queue
<Thread(Thread-3, started 139824329647872)> removed ('5', 'tomato') from the queue

"""