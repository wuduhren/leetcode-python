"""
Time: O(NLogN),
The root need to traverse N node to get its midNode.

The root.left need to traverse N/2 node to get its midNode.
The root.right need to traverse N/2 node to get its midNode.

The root.left.left need to traverse N/4 node to get its midNode.
The root.left.right need to traverse N/4 node to get its midNode.
The root.right.left need to traverse N/4 node to get its midNode.
The root.right.right need to traverse N/4 node to get its midNode.

...
So total:
N + (N/2+N/2) + (N/4+N/4+N/4+N/4) + ... => N + N + N + ...
There are LogN levels in the tree, so LogN x N => NLogN

Space: O(LogN) for recursion depth.
"""
class Solution(object):
    def sortedListToBST(self, head):
        if not head: return None
        
        midNode = self.getMiddle(head)
        root = TreeNode(midNode.val)
        
        if head.val==midNode.val: return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(midNode.next)
        
        return root
    
    def getMiddle(self, node):
        pre = None
        slow = node
        fast = node

        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next

        if pre: pre.next = None
        return slow