import queue

def task(task_name, work_queue):
    if work_queue.empty():
        print(f"Nothing to do in task : {task_name}")
    else:
        while not work_queue.empty():
            print(f"Task {task_name} is running...")
            work = work_queue.get()
            count = 0
            for i in range(work):
                count += 1
            print(f"Ran the task: {task_name} total: {count}")


def main():
    # create work queue
    work_queue = queue.Queue()
    
    # put the work
    for work in [2, 4, 5, 6]:
        work_queue.put(work)
        
    # create some synchronous tasks
    tasks = [("One", work_queue), ("Two", work_queue)]
    
    # do tasks 
    for t, q in tasks:
        task(t, q)
    


if __name__ == "__main__":
    main()