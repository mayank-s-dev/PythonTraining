# multi threading and multiprocessing

"""
In multi threading
    process is parent
    threads are child, which uses parents resources
    threads are manage by pythin
    We use threading when there is time bound IO operation

In multiprocessing
    there will be multiple processes and each process has it own resources are assigned to it
    We use multiprocessing when there is CPU bound task


"""
import time
from threading import Thread
from multiprocessing import Process


def intro():
    print("Hello")
    time.sleep(1)
    print("1 secs completed")


"""
start = time.time()
intro()
intro()
end = time.time()

print("Time taken: ", end - start)
"""

# we can use the thread when the process is sleep

# assigning target to threads
"""
thread_start_time = time.time()
thread1 = Thread(target=intro)
thread2 = Thread(target=intro)

thread1.start()
thread2.start()
thread1.join()
thread2.join()

thread_end_time = time.time()

print("Multi threading took:", thread_end_time - thread_start_time)
"""

'''
Steps we performed:
- define thread object with targeted function
- start the thread
- join the thread
'''

# MULTIPROCESSING
'''
What are CPU intensive task: which requires lot of CPU time
to work with multiprocessing, you first need to know how many cores your processor have

process comes with some overhead time of their own
'''


def hello(start, end):
    print("Started", start, end, Process.pid)
    result = []
    for i in range(start, end):
        result.append(i * i)

    print("Calculated squares", Process.pid)


start_hello = time.time()
hello(1, 1000001)
hello(1, 1000001)
end_hello = time.time()
print("Time taken to run hello", end_hello - start_hello)

# doing multiprocessing

"""
if __name__ == '__main__':
    process_start_time = time.time()
    process1 = Process(target=hello)
    process2 = Process(target=hello)
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    process_end_time = time.time()

    print("Time taken by multiprocessing to run hello", process_end_time - process_start_time)
"""

if __name__ == '__main__':
    start = time.time()
    process1 = Process(target=hello, args=(1, 500001))
    process2 = Process(target=hello, args=(500001, 1000000))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    end = time.time()
    print("Time taken by multiprocessing to run hello", end-start)