
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue is full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return

        value = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return value

    def display(self):
        print(self.queue)


q = CircularQueue(3)

# q.enqueue(11)
# q.enqueue(22)
# q.enqueue(33)

# q.display()
