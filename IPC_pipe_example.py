import os, sys
import multiprocessing

class ChildProcess(multiprocessing.Process):

    def __init__(self,pipe):
        super(ChildProcess, self).__init__()
        self.pipe = pipe

    def run(self):
        print("Attempting to pipein to pipe")
        with os.fdopen(self.pipe, 'w') as pipe:
            pipe.write("This is pipe data, I am sending to my Parent")
            pipe.close()

def main():
    pipeout, pipein = os.pipe()
    child = ChildProcess(pipein)
    child.start()
    child.join()
    os.close(pipein)
    pipeout = os.fdopen(pipeout)

    pipedata = pipeout.read()
    print("This is Pipe: {} ".format(pipedata))

main()