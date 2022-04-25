class Solution(object):
    def removeNthFromEnd(self, head, n):
        def getCount(node0):
            curr = node0
            count = 0
            while curr:
                curr = curr.next
                count += 1
            return count
        
        def removeNext(node0):
            nextNode = node0.next
            if not nextNode: return
            node0.next = nextNode.next
        
        k = getCount(head)-n-1 #need to "curr = curr.next" k times to reach the node that we can call removeNext(curr)
        if k==-1: return head.next #remove head
        
        curr = head
        while k>0:
            k -= 1
            curr = curr.next
        
        removeNext(curr)
        return head