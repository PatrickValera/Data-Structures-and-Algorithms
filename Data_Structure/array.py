# Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
# T - Trivial; did not implement
# X - Done

# []  New raw data array with allocated memory
#       can allocate int array under the hood, just not use its features
#       start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
# [X]  size() - number of items
# [T]  capacity() - number of items it can hold
# [T]  is_empty()
# [X]  at(index) - returns item at given index, blows up if index out of bounds
# [X]  push(item)
# [X]  insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
# [T]  prepend(item) - can use insert above at index 0
# [X]  pop() - remove from end, return value
# [X]  delete(index) - delete item at index, shifting all trailing elements left
# [X]  remove(item) - looks for value and removes index holding it (even if in multiple places)
# [X]  find(item) - looks for value and returns first index with that value, -1 if not found
# []  resize(new_capacity) // private function
#       when you reach capacity, resize to double the size
#       when popping an item, if size is 1/4 of capacity, resize to half

class Vector:
    def __init__ (self,capacity):
        self.capacity=capacity
        self.array=[]*capacity
    def print(self):
        for elem in self.array: print(elem,  end='-')
    def size(self):
        return len(self.array)
    def at(self,index):
        if self.size()-1<index:
            # print('Index Error')
            return('Index out of bounds')
        return self.array[index]
    def push(self,data):
        print(self.size())
        if self.size()>=self.capacity:
            print('RESIZE')
            # self.resize(self.size()*2)
        # self.array[self.size()]=data
        self.array.append(data)
    def insert(self,index,data):
        if self.size()>=self.capacity:
            self.resize(self.size()*2)
        if self.size()-1<index:
            print('Index out of bounds')
            return
        self.push('temp')
        temp2=data
        for x in range(index,self.size()):
            temp=self.array[x]
            self.array[x]=temp2
            temp2=temp
    def pop(self):
        return self.array.pop()
    def delete(self,index):
        self.push('temp')
        for x in range(index,self.size()-1):
            self.array[x]=self.array[x+1]
        self.pop()
        self.pop()
    def remove(self,data):
        index=0
        end=self.size()
        while index<end:
            if self.array[index]==data:
                self.delete(index)
                index-=1
                end-=1
                if index<0:index=0
            else:index+=1
    def find(self,data):
        for index,x in enumerate(self.array):
            if x==data:return index
        return -1
    def resize(self,new_capacity):
        ar=[]*(new_capacity)
        for index,x in enumerate(self.array):
            ar[index]=x
        self.array=ar

        

vector=Vector(4)
vector.push(0)
vector.push(1)
vector.push(2)
vector.push(1)
vector.push(1)
# vector.push(1)
# vector.push(1)
# vector.push(2)
# vector.push(3)
# vector.insert(2,2)
# vector.pop()
# vector.delete(1)
# vector.remove(1)
# print(vector.find(1))
vector.print()
# print(vector.at(0))