import queue
import time


def do_task(doer_name, work):
    thing_in_hand = work.get()
    print(f"Worker: {doer_name} work : {thing_in_hand}")
    print(f"Worker {doer_name} starting the work...")
    yield
    
    for i in range(thing_in_hand):
        print(f"Worker {doer_name} doing the work by {i}...")
        time.sleep(i)
            
    if work.empty():
        print(f"Worker: {doer_name} has no work to do...")

def main():
    # create a queue
    work_queue = queue.Queue()
    
    # put work
    for work in [4, 5, 6, 7]:
        work_queue.put(work)
        
    # task doers
    doers = [("Doer_one", work_queue), ("Doer_two", work_queue)]
        
    # do the work
    is_working = True
    while is_working:
        for doer in doers:
            work_gens = do_task(doer[0], doer[1])
            try:
                next(work_gens)
            except StopIteration:
                print("Iteration stopped!")
    print("Fininsed...")


if __name__ == "__main__":
    main()