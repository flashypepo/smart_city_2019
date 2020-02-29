"""
Example Queue

A queue is a linear data structure that follows the
First In First Out (FIFO) principle.

A good example is a queue of customers that are
waiting in line, where the customer that came
first is served first.

Queues can be used for thread-safe/process-safe data
exchanges and data processing both in a multithreaded
and a multiprocessing environment.

2020-0225 PP new
"""
from queue import Queue

# create queue
q = Queue()

# add elements
q.put(1)  # 1
q.put(2)  # 2 1
q.put(3)  # 3 2 1

# now q looks like this:
# back --> 3 2 1 --> front
print(q.queue)

# get and remove first element
first = q.get()  # --> 1
print(first)

# q looks like this:
# back --> 3 2 --> front
print(q.queue)
