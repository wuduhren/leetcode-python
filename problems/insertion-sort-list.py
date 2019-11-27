# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, node):
        """
        `pre_head` is a common technique that used in linked list problem.
        So we don't need to handle the edge case all the time.
        """
        pre_head = ListNode(float('-inf'))
        pre_head.next = node
        pre = pre_head
        while node:
            if node.val>=pre.val: #see if node need to shift, if true, no need to shift this node
                pre = node
                node = node.next
            else:
                next_node = node.next
                self.remove(pre, node)
                self.insert(pre_head, node)
                node = next_node
        return pre_head.next

    def remove(self, pre, node):
        pre.next = node.next

    def insert(self, pre_head, node):
        curr = pre_head.next
        pre = pre_head
        while curr:
            if node.val<curr.val:
                pre.next = node
                node.next = curr
                break
            pre = curr
            curr = curr.next
        