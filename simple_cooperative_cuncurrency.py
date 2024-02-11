import queue


def do_work(task_name, work_queue):
    while not work_queue.empty():
        work = work_queue.get()
        count = 0
        print(f"Running task {task_name}...")
        for i in range(work):
            count += 1
            # yield between each mini action in task
            yield
        print(f"Task {task_name} is done with total : {count}")
        

def main():
    # create queue
    work_queue = queue.Queue()
    
    # add work
    for work in [5, 4, 7, 9, 11, 67, 34]:
        work_queue.put(work)
        
    # create tasks
    tasks = [("T1", work_queue), ("T2", work_queue)]
    
    li = []
    # loop through it(does the initial run - until count)
    for t, w in tasks:
        li.append(do_work(t, w))
        
    # run tasks
    done = False
    while not done:  
        for i in li:
            try:
                next(i)
            except StopIteration:
                li.remove(i)
                # print(StopIteration)
        if len(li) == 0:
            done = True
            

if __name__ == "__main__":
    main()