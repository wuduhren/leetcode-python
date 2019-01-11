#https://leetcode.com/problems/sort-list/
class Solution(object):
    
    #sortList() is going to return sorted linked list
    #it will split the linked list into two
    #the head and the second_half
    #put each of them to sortList() again
    #merge two sorted list, then return
    def sortList(self, head):
        if head==None or head.next==None:
            return head
        
        #find mid point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        head = self.sortList(head)
        second_half = self.sortList(second_half)
        
        return self.merge(head, second_half)
    
    
    #merge two sorted linked list
    #return one sorted linked list
    #in this case, the linked list is going to be splited into half and half and hald...
    #eventually only one node left (which is of course sorted)
    #one node goes to l1, another node goes to l2
    #returning a sorted 2 nodes linked list
    #then two 2 nodes linked list goes to l1 and l2
    #returning a sorted 4 nodes linked list
    #...and so on
    def merge(self, l1, l2):
        if l1==None and l2==None:
            return None
        elif l1 and l2==None:
            return l1
        elif l1==None and l2:
            return l2
        
        pre = ListNode(None)
        curr = pre
        
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return pre.next
                
#Efficiency: O(NLogN)
#Space: O(N)