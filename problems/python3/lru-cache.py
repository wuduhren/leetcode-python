class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
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

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.promote(node)
            return node.val
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.promote(node)
        self.dic[key] = node
        
        if len(self.dic)>self.capacity: #[2]
            del self.dic[self.tail.prev.key]
            self.remove(self.tail.prev)
