class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.l = []

    def get(self, index):
        if index<0 or index>=len(self.l):
            return -1
        return self.l[index].val

    def addAtHead(self, val):
        self.l = [Node(val)]+self.l

    def addAtTail(self, val):
        self.l = self.l+[Node(val)]

    def addAtIndex(self, index, val):
        self.l = self.l[:index]+[Node(val)]+self.l[index:]

    def deleteAtIndex(self, index):
        self.l = self.l[:index]+self.l[index+1:]
