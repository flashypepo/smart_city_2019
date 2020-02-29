"""
Example multi-threading to illustrate (simple) concurrency
source: https://www.python-engineer.com/blog/advancedpython16_threading

2020-0225 PP new
"""
from threading import Thread, current_thread


# def square_numbers(nr):
def square_numbers():
    for i in range(1000):
        result = i * i
    print(f"in {current_thread().name} result={result}")


if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads and asign a function for each thread
    for i in range(num_threads):
        thread = Thread(name=f"Thread{i+1}", target=square_numbers)
        threads.append(thread)

    # start all threads
    for thread in threads:
        thread.start()

    # wait for all threads to finish
    # block the main thread until these threads are finished
    for thread in threads:
        thread.join()

    print('main done')
