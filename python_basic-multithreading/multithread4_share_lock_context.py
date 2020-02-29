"""
Example multi-threading to illustrate (simple) concurrency
Lock shared data between threads with context manager.

source: https://www.python-engineer.com/blog/advancedpython16_threading

2020-0225 PP new
"""
from threading import Thread, Lock
import time

# global data accessible by all threads
database_value = 0


# After lock.acquire() you should never forget
# to call lock.release() to unblock the code.
# You can also use a lock as a context manager,
# wich will safely lock and unlock your code.
def increase(lock):
    global database_value

    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


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
