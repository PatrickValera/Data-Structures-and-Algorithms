# Insertion O(1)
# Deletion O(1)
# Insert at end O(n)

#  [X] size() - returns number of data elements in list
#  [X] empty() - bool returns true if empty
#  [X] value_at(index) - returns the value of the nth item (starting at 0 for first)
#  [X] push_front(value) - adds an item to the front of the list
#  [X] pop_front() - remove front item and return its value
#  [X] push_back(value) - adds an item at the end
#  [T] pop_back() - removes end item and returns its value
#  [T] front() - get value of front item
#  [T] back() - get value of end item
#  [X] insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
#  [X] erase(index) - removes node at given index
#  [] value_n_from_end(n) - returns the value of the node at nth position from the end of the list
#  [X] reverse() - reverses the list
#  [] remove_value(value) - removes the first item in the list with this value
class Node:
    def __init__ (self,data=None,next=None):
        self.next=next
        self.data=data

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def empty(self):
        if self.head:
            return False
        else:
            return True

    def value_at_index(self,index):
        cntr=0
        itr=self.head
        while cntr != index:
            cntr+=1
            itr=itr.next
        return itr.data

    def pop_front(self):
        val=self.head.data
        self.head=self.head.next
        return val
            
    def insert(self,data,index):
        cntr=0
        itr=self.head
        while cntr!=index-1:
            cntr+=1
            itr=itr.next
        new_node=Node(data,itr.next)
        itr.next=new_node

    def erase(self,index):
        return
        # cntr=0
        # prev=None
        # itr=self.head
        # next=None
        # while cntr!=index:
        #     cntr+=1
        #     itr=itr.next
        # itr.next=itr.next.next

    def reverse(self):
        prev=None
        curr=self.head
        next=None
        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        
    def remove_value(self,value):
        cntr=0
        if self.head is not None:
            itr=self.head
            while itr.data != value:
                itr=itr.next
                cntr+=1
            self.erase(cntr)

    def insert_at_start(self,data):
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self,data=None):
        if self.head is None:
            self.head=Node(data)
        else:
            end=self.head
            while end.next:
                end=end.next
            end.next=Node(data)
    def print_list(self):
        if self.head is None:
            print('linked list is empty')
        else:
            itr=self.head
            while itr is not None:
                print(itr.data , end = ' -> ')
                itr=itr.next
        print("\n")

list=LinkedList()
list.insert_at_start(1)
list.insert_at_end(3)
list.insert_at_end(4)
list.insert(2,1)
# list.erase(3)
# list.reverse()
list.remove_value(1)
list.print_list()
print('empty:',list.empty())
print('size:',list.size())
print('value at index 1:',list.value_at_index(1))
print('pop front:',list.pop_front())
list.print_list()
