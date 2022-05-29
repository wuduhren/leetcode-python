class Solution(object):
    def insert(self, random, insertVal):
        def allValSame(node):
            curr = node.next
            while curr!=node:
                if curr.val!=node.val: return False
                curr = curr.next
            return True
                
        newNode = Node(insertVal)
        
        #handle null linked list
        if not random:
            newNode.next = newNode
            return newNode
        
        #handle linked list with val all the same
        if allValSame(random):
            temp = random.next
            random.next = newNode
            newNode.next = temp
            return random
        
        #find head and tail, head is the min val node, tail is the max val node.
        curr = random
        while curr.val<=curr.next.val:
            curr = curr.next
        tail = curr
        head = curr.next
        
        #insert new node
        if insertVal>=tail.val or insertVal<=head.val:
            tail.next = newNode
            newNode.next = head
        else:
            curr = head
            while not curr.val<=insertVal<=curr.next.val: curr = curr.next
            temp = curr.next
            curr.next = newNode
            newNode.next = temp
        
        return random