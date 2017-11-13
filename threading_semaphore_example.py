import time
import threading
import random

total_fund = 80


class Fundraiser(threading.Thread):


    def __init__(self, semaphore, name):
        threading.Thread.__init__(self)
        self.sema = semaphore
        self.name = name
        self.fundraised = 0
        print("Fundraiser started work")

    def run(self):
        global total_fund
        running = True
        while running:
            time.sleep(random.randint(0,1))
            self.sema.acquire()
            if total_fund <= 0:
                # Dont have fund, stop fundraiser
                running = False
            else:
                self.fundraised += 1
                total_fund -= 1
                print("{} fund raised million, {} million available".format(self.getName(), total_fund))
            self.sema.release()
        print("{} raised Total {} million fund".format(self.getName(), self.fundraised))

def main():

    semaphore = threading.Semaphore()

    # Total fund available in million
    print("Total available fund in million is {}".format(total_fund))
    raiser = []
    # Array of fundraiser
    fundraisers = ["Mike","Tendua", "Jason","Kelly", "Sarah", "Samantha","Daisy", "Randy", "Josh","Lisa","Barron"]

    for person in fundraisers:
        person = Fundraiser(semaphore,person)
        person.start()
        raiser.append(person)

    for i in raiser:
        i.join()

main()