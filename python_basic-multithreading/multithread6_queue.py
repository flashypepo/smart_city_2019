#!/usr/bin/env python
"""
Example multi-threading to illustrate (simple) concurrency

Operations with a queue are thread-safe.
Important methods are:

q.get() : Remove and return the first item.
          By default, it blocks until the item is available.
q.put(item) : Puts element at the end of the queue.
          By default, it blocks until a free slot is available.
q.task_done() : Indicate that a formerly enqueued task is complete.
          For each get() you should call this after you are done
          with your task for this item.
q.join() : Blocks until all items in the queue have been gotten
           and proccessed (task_done() has been called for each item).
q.empty() : Return True if the queue is empty.

The following example uses a queue to exchange numbers
from 0...19. Each thread invokes the worker method.

Inside the infinite loop the thread is waiting until
items are available due to the blocking q.get() call.

When items are available, they are processed
(i.e. just printed here), and then q.task_done()
tells the queue that processing is complete.

In the main thread, 10 daemon threads are created.
This means that they automatically die when the main
thread dies, and thus the worker method and
infinite loop is no longer invoked.

Then the queue is filled with items and the worker method
can continue with available items.

At the end q.join() is necessary to block the main
thread until all items have been gotten and proccessed.

NOTE:
In the example, daemon threads are used.
Daemon threads are background threads that automatically die
when the main program ends. This is why the infinite loops inside the worker
methods can be exited.

Without a daemon process we would have to use a signalling mechanism
such as a threading.Event to stop the worker. But be careful with
daemon processes: They are abruptly stopped and their resources
(e.g. open files or database transactions) may not be
released/completed properly.

source: https://www.python-engineer.com/blog/advancedpython16_threading

2020-0229 PP extended as a correct and testable program,
             source: Tiny Python Projects, manning.com, 2020
2020-0225 PP new
"""
from threading import Thread, Lock, current_thread
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()  # blocks until the item is available

        # do stuff...
        with lock:
            # prevent printing at the same time with this lock
            print(f"in {current_thread().name} got {value}")
        # ...

        # For each get(), a subsequent call to task_done() tells the queue
        # that the processing on this item is complete.
        # If all tasks are done, q.join() can unblock
        q.task_done()


if __name__ == '__main__':
    q = Queue()
    num_threads = 10
    lock = Lock()

    for i in range(num_threads):
        t = Thread(name=f"Thread{i+1}", target=worker, args=(q, lock))
        t.daemon = True  # dies when the main thread dies
        t.start()

    # fill the queue with items
    for x in range(20):
        q.put(x)

    # Blocks until all items in the queue have been gotten and processed.
    q.join()

    print('main done')
