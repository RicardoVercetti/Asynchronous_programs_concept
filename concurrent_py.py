# learning concurrency and context switching
import queue
import time
from codetiming import Timer


def task(name, w_queue):
    timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
    while not w_queue.empty():
        delay = w_queue.get()
        # total = 0
        print(f"Task {name} is running...")
        # total += 1
        timer.start()
        time.sleep(delay)
        timer.stop()
        yield
        # print(f"Task {name} Total: {total}")


def main():
    # create a queue
    work_queue = queue.Queue()
    
    # put some work
    for work in [4, 5, 7, 6]:
        work_queue.put(work)
    
    # create some tasks
    tasks = [task("One", work_queue), task("Two", work_queue)]
    
    # Run the tasks
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
                
            if len(tasks) == 0:
                done = True
            
            



if __name__ == "__main__":
    main()

