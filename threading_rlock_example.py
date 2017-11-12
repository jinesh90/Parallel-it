"""
Rlock is another method to lock threads, its different than traditional lock
Rlock is safer than lock.more info
check this: https://stackoverflow.com/questions/22885775/
"""

import time
import threading

class Worker():
    def __init__(self):
        self.a = 1
        self.b = 2
        # define R lock, if you use Lock here, program will stuck into deadlock, think how?
        self.Rlock = threading.RLock()

    def modifyA(self):
        # Syntax for use rlock, alternatively user can use self.Rlock.acquired()
        with self.Rlock:
            print("Now modifying variable A: Rlock acquired")
            self.a = self.a + 1
            time.sleep(1)

    def modifyB(self):
        with self.Rlock:
            print("Now modifying variable B: Rlock acquired")
            self.b = self.b -1
            time.sleep(1)

    def modifyBoth(self):
        with self.Rlock:
            print("Now modifying both variable A and B: Rlock acquired")
            self.modifyA()
            self.modifyB()


def main():
    worker = Worker()
    worker.modifyBoth()

main()


