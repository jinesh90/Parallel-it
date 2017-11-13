"""
Events are easy way to pass information between two threads or control threads with a single shared event object
This example shows how to use event for wait in thread.
"""

import threading
import time
import random


def thread_with_event(event):
    counter = 0
    while not event.is_set():
        counter += 1
        print("Event is not set yet, Waiting , increasing counter to {}".format(counter))
        time.sleep(1)
    print("event is set after counting {}".format(counter))


def main():
    event = threading.Event()
    thread1 = threading.Thread(target=thread_with_event, args=(event,))
    thread1.start()
    sleep_time = random.randint(10, 50)
    print("Sleeping Time set to {}".format(sleep_time))
    time.sleep(sleep_time)

    # after some random delay, set event
    event.set()


main()
