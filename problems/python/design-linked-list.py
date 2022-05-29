class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.l = [] #trade space for speed

    def get(self, index): #O(1)
        if index<0 or index>=len(self.l):
            return -1
        return self.l[index].val

    def addAtHead(self, val): #O(N), list extend takes O(N), <https://wiki.python.org/moin/TimeComplexity>.
        self.l = [Node(val)]+self.l

    def addAtTail(self, val): #O(N)
        self.l = self.l+[Node(val)]

    def addAtIndex(self, index, val): #O(N)
        self.l = self.l[:index]+[Node(val)]+self.l[index:]

    def deleteAtIndex(self, index): #O(N)
        self.l = self.l[:index]+self.l[index+1:]
