"""
I learned this answer from @tusizi; rewrote it.

Let's analyze the problem
If we need get() to be O(1),
we must definitely use a hashmap(dictionary) to store the key value.

put() is not a problem, since we are only setting value.
The problem is when we excceed the capacity.
How do we find the least-used key and remove it from the hashmap?
We need something for us to sort from most-frequent-used to least-used.

So what else common data structure do we know?
Array? no, we will need to iterate to the whole array to find what we need. and it is not easy to add or remove.
Tree? not likely.
Min-heap? even though we can get the least-used, but it need O(LogN) to set the most-frequent-used.
Link list? Bingo!

We also need it to be a double link list, so we can remove the tail.
We also need the node to store the key when we remove the tail, we can also remove it in the hashmap
We also need the node to store the val when we get().

It would be like:
head<->node1<->node2<->node3 ... nodeN<->tail
(most-frequent-used to least-used)

So the main idea now is to use hashmap to store the key:Node pair [0]
If we put or get any key-value pair, we move its node to the front of the line (I call this promote()) [1]
The front of the line means we put it just after head.
If we excced the capacity, we remove the node at the end of the line [2]
The end of the line means the node just before tail.

The head and tail is just a dummy, [3]
for us to keep track of the first and the last of the linklist
and don't have worry about the edge case.
"""
class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {} #[0]
        self.head = Node(0, 0) #[3]
        self.tail = Node(0, 0) #[3]
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def promote(self, node): #[1]
        #set the node next to head
        temp = self.head.next
        node.next = temp
        temp.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.promote(node)
            return node.val
        return -1
            
    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.promote(node)
        self.dic[key] = node
        
        if len(self.dic)>self.capacity: #[2]
            del self.dic[self.tail.prev.key]
            self.remove(self.tail.prev)

#using OrderedDict()
class LRUCache(object):
    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.remain = capacity

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v   # set key as the newest one
        return v

    def set(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value