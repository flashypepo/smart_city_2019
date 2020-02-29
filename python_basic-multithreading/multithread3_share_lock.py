"""
Example multi-threading to illustrate (simple) concurrency
Lock shared data between threads

source: https://www.python-engineer.com/blog/advancedpython16_threading

2020-0225 PP new
"""
# import Lock
from threading import Thread, Lock
import time

# global data accessible by all threads
database_value = 0


def increase(lock):
    global database_value

    # lock the state
    lock.acquire()

    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy

    # unlock the state
    lock.release()


if __name__ == "__main__":

    # create a lock
    lock = Lock()

    print('Start value: ', database_value)

    # pass the lock to the target function
    # notice the comma after lock since args must be a tuple
    t1 = Thread(target=increase, args=(lock,))
    t2 = Thread(target=increase, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)
