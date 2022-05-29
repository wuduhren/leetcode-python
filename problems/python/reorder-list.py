"""
The reorder list, we can see it as
smallest, largest, 2th smallest, 2th largest, 3th smallest...

First, put the ordered nodes in a stack, so we can get the largest node by `pop()`.
And count how many nodes in total.

Second, because the node is already ordered
So we only need to insert a large node between every node until we hit the count.

Last, remember to put `None` at the end.

The tricky part is there may be even count or odd count of nodes in total.
When face problem like this, you should approach these test cases by hand.
Think about the edge cases. Here:
1->2->3->4
1->2->3->4->5
"""
class Solution(object):
    def reorderList(self, head):
        if head is None: return
        h = head
        curr = head
        stack = []
        count = 0

        while curr:
            count+=1
            stack.append(curr)
            curr = curr.next

        while count>1:
            temp = h.next
            h.next = stack.pop()
            h.next.next = temp
            count-=2
            h = h.next.next

        h.next = None
