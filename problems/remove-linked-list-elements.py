#https://leetcode.com/problems/remove-linked-list-elements/
class Solution(object):
    def removeElements(self, head, val):
        if head is None:
            return head
        
        #check head
        if head.val==val:
            return self.removeElements(head.next, val)
        
        current = head
        
        while current and current.next:
            #save the current node on prev
            #move current to next node
            prev = current
            current = current.next
            
            if current.val==val:
                #remove
                prev.next = current.next
                current = prev
                
        return head