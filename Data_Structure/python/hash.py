# [X] hash(k, m) - m is size of hash table
# [X] add(key, value) - if key already exists, update value
# [X] exists(key)
# [X] get(key)
# [X] remove(key)

class Node:
    def __init__(self,key,value) -> None:
        self.key=key
        self.value=value
        self.next=None

class Hash:
    def __init__(self,capacity) -> None:
        self.capacity=capacity
        self.size=0
        self.buckets=[None]*capacity

    def hash(self,key):
        hash_sum=0
        for indx,char in enumerate(key):
            hash_sum+=(indx+len(key)**ord(char))
        hash_sum%=self.capacity
        return hash_sum

    def add(self,key,value):
        self.size+=1
        index=self.hash(key)
        node=self.buckets[index]
        if node is None:
            self.buckets[index]=Node(key,value)
        else:
            itr=node
            while itr.next is not None:
                itr=itr.next
            itr.next=Node(key,value)
    def exists(self,key):
        index=self.hash(key)
        if self.buckets[index] is not None:
            return True
        return False
    def get(self,key):
        index=self.hash(key)
        if self.exists(key):
            return self.buckets[index].value
    def remove(self,key):
        if self.exists(key):
            self.buckets[self.hash(key)]=None

hash=Hash(10)

hash.add('weight',165)
hash.remove('weight')
print(hash.exists('weight'))
print(hash.get('weight'))