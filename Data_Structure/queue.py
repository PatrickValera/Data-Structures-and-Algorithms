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

queue=Queue_Linked_List()
queue.enqueue(1)
queue.enqueue(2)
queue.dequeue()
queue.dequeue()
print(queue.empty())