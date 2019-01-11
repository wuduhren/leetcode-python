#https://leetcode.com/problems/merge-two-sorted-lists/
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1==None and l2==None:
            return None
        elif l1 and l2==None:
            return l1
        elif l1==None and l2:
            return l2
        
        pre = ListNode
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