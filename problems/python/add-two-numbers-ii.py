"""
First, if you haven't done the [first problem](https://leetcode.com/problems/add-two-numbers/) please do it first. And here is its [answer](https://leetcode.com/problems/add-two-numbers/discuss/43105).
We can just reverse the linked list, and we can use the solution of the [first problem](https://leetcode.com/problems/add-two-numbers/).
So I do this problem without reversing the linked list.

We need to know the length of each linked list. So we can know when do we start adding the `val`.
We need to set the answer to a double linked list. Because we might need to modify the upper digits.
For example 999 + 1.

The time complexity is `O(N)`, `N` is the length of the input linked list.
The space complexity is `O(N)`, too.
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution(object):
    def addTwoNumbers(self, A, B):
        l1 = self.getLength(A)
        l2 = self.getLength(B)
        head = ListNode(0)
        curr = head
        while A or B:
            if l1>l2:
                self.addDigit(curr, A.val)
                l1-=1
                A = A.next
            elif l2>l1:
                self.addDigit(curr, B.val)
                l2-=1
                B = B.next
            else:
                val = (A.val if A else 0) + (B.val if B else 0)
                self.addDigit(curr, val)
                if l1: l1-=1
                if l2: l2-=1
                if A: A = A.next
                if B: B = B.next
            curr = curr.next
        return head if head.val else head.next #remove leading zero

    def getLength(self, L):
        length = 0
        while L:
            length+=1
            L = L.next
        return length

    def addDigit(self, node, val):
        if val<10:
            node.next = ListNode(val)
            node.next.prev = node
        else:
            node.next = ListNode(val-10)
            node.next.prev = node
            node.val+=1
            while node.val>=10:
                node.prev.val+=1
                node.val-=10
                node = node.prev
