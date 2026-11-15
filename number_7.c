
#include <stdio.h>
#define SIZE 5

int deque[SIZE];
int front = -1, rear = -1;

int isFull() {
    return (front == (rear + 1) % SIZE);
}

int isEmpty() {
    return (front == -1);
}

// Front insertion
void insertFront(int x) {
    if (isFull()) {
        printf("Deque is full\n");
        return;
    }

    if (isEmpty())
        front = rear = 0;
    else
        front = (front - 1 + SIZE) % SIZE;

    deque[front] = x;
}

// Rear insertion
void insertRear(int x) {
    if (isFull()) {
        printf("Deque is full\n");
        return;
    }

    if (isEmpty())
        front = rear = 0;
    else
        rear = (rear + 1) % SIZE;

    deque[rear] = x;
}

// Front deletion
void deleteFront() {
    if (isEmpty()) {
        printf("Deque is empty\n");
        return;
    }

    printf("Deleted: %d\n", deque[front]);

    if (front == rear)
        front = rear = -1;
    else
        front = (front + 1) % SIZE;
}

// Rear deletion
void deleteRear() {
    if (isEmpty()) {
        printf("Deque is empty\n");
        return;
    }

    printf("Deleted: %d\n", deque[rear]);

    if (front == rear)
        front = rear = -1;
    else
        rear = (rear - 1 + SIZE) % SIZE;
}

int main() {
    insertRear(10);
    insertRear(20);
    insertFront(5);

    deleteFront();
    deleteRear();

    return 0;
}
