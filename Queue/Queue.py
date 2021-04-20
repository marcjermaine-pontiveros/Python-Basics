from QueueInterface import QueueInterface 
from QueueExceptions import QueueEmptyException, QueueFullException 
from Node import Node 

class LinkedQueue(QueueInterface): 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self._size = 0

    def size(self): 
        return self._size 

    def isEmpty(self):
        return self.head == None 

    def front(self): 
        if self.isEmpty(): 
            raise QueueEmptyException("Queue is empty!") 

        return self.head.data 

    def enqueue(self):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next 
        self._size += 1

    def dequeue(self):
        data = self.front()
        self.head = self.head.next 
        self._size -= 1 
        return data 

class ArrayQueue(QueueInterface):
    DEFAULT_CAPACITY = 5 

    def __init__(self, capacity = None):
        self._front = 0 
        self._size = 0 
        self.rear = 0     
        self.capacity = ArrayQueue.DEFAULT_CAPACITY if capacity is None else capacity     
        self.data = [None]*self.capacity 

    def size(self):
        return self._size 
    
    def enqueue(self, datum):
        if self.isFull():
            raise QueueFullException("Queue overflow! Maximum size: {}.".format(self.capacity)) 
        self.data[self.rear] = datum     
        self._size = self._size + 1
        self.rear = (self.rear + 1)%self.capacity

    def dequeue(self): 
        result = self.front() 
        self.data[self._front] = None 
        self._front = (self._front + 1)%self.capacity 
        self._size = self._size - 1 
        return result 

    def front(self): 
        if self.isEmpty(): 
            raise QueueEmptyException("Queue underflow!") 
        return self.data[self._front] 
    
    def isEmpty(self): 
        return self._front == self.rear 
    
    def isFull(self): 
        return (self._front == (self.rear+1)%self.capacity) 