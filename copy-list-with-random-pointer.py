# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution(object):
    def copyRandomList(self, head):
        if head==None: return head
        
        curr = head
        while curr:
            temp = curr.next
            new_node = RandomListNode(curr.label)
            new_node.next = temp
            curr.next = new_node
            curr = curr.next.next
            
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
            
        curr = head
        curr_copy = head.next
        head_copy = head.next
        
        while curr:
            curr.next = curr.next.next
            curr_copy.next = curr_copy.next.next if curr_copy.next else None
            curr = curr.next
            curr_copy = curr_copy.next
            
        return head_copy