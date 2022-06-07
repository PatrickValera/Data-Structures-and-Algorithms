# IMPLEMENT THE FOLLOWING FOR BOTH ARRAY AND LINKED LIST IMPLEMENATION
# [X] enqueue(value) - adds value at position at tail
# [X] dequeue() - returns value and removes least recently added element (front)
# [X] empty()
# [] full() - for array implementation
from linkedlist import LinkedList,Node

class Queue_Linked_List:
    def __init__(self) -> None:
        self.head = None
    def enqueue(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr=self.head
            while itr.next is not None:
                itr=itr.next
            itr.next=Node(data)
    def dequeue(self):
        if self.head is not None:
            self.head=self.head.next
    def empty(self):
        if self.head is not None:
            return False
        return True

class Queue_Array:
    def __init__(self,capacity):
        self.capacity=capacity+1
        self.list=[None]*capacity
        self.ptr=0
        self.start=0
        self.end=0
    def enqueue(self,data):
        if self.full():return
        self.list[self.ptr]=data
        self.ptr+=1
        self.end+=1
    def dequeue(self):
        if self.empty():return
        self.start+=1
    def empty(self):
        if self.start==self.end:return True
        else: return False
    def full(self):
        print(self.start,self.end)
        if self.empty():return False
        if self.start==(self.end-1):
            print('list full')
            return True
        else: return False
    def print(self):
        start=self.start
        while start!=self.end:
            print(self.list[start])
            start+=1

#LINKED LIST IMPLEMENTATION
# queue=Queue_Linked_List()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.dequeue()
# queue.dequeue()
# print(queue.empty())

#ARRAY IMPLEMENTATION
array=Queue_Array(5)
array.enqueue(1)
array.enqueue(2)
array.enqueue(3)
array.enqueue(4)
array.enqueue(5)
# array.enqueue(5)
# array.dequeue()
array.print()