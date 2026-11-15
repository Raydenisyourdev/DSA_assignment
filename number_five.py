
queue = []
size = 5

def enqueue(item):
    if len(queue) == size:
        print("Queue is full")
    else:
        queue.append(item)
        print(item, "inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print(queue.pop(0), "removed")

def display():
    print("Queue:", queue)


enqueue(10)
enqueue(20)
enqueue(30)

display()

dequeue()

display()
