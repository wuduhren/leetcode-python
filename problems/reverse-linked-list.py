#https://leetcode.com/problems/reverse-linked-list/
# class Solution(object):
#     #iterative
#     def reverseList(self, head):
#         prev = None
#         current = head
#         while current:
#             temp = current.next
#             current.next = prev
#             prev = current
#             current = temp

#         return prev

#     #recursive
#     def reverseList(self, head):
#         if head is None or head.next is None:
#             return head

#         new_head = self.reverseList(head.next)
#         n = head.next
#         n.next = head
#         head.next = None
#         return new_head

#recursive
class Solution(object):
    def reverseList(self, node):
        if node and node.next:
            new_head = self.reverseList(node.next)
            node.next.next = node
            node.next = None
            return new_head
        return node

#iterative
class Solution(object):
    def reverseList(self, node):
        pre = None
        while node:
            next_node = node.next
            node.next = pre
            if not next_node: return node
            pre = node
            node = next_node
