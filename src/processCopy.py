import os
import time

def createSonProcess(numberOfChildProcesses):
    for i in range(numberOfChildProcesses):
        pid = os.fork()
        if pid == 0:
            print("Child process created with PID: ", os.getpid())
            time.sleep(5)
            print("Child process with PID: ", os.getpid(), "finished")
            os._exit(0)
        else:
            print("Parent process created with PID: ", os.getpid())

if __name__ == "__main__":
    numberOfChildProcesses = int(input("Enter the number of child processes to create: "))
    createSonProcess(numberOfChildProcesses)
