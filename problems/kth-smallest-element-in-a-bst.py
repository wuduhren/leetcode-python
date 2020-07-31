class Solution(object):
    def kthSmallest(self, root, k):
        count = 0
        stack = []
        node = root
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            count += 1
            
            if count==k: return node.val
            
            node = node.right
            
        return 0

"""
Time complexity: O(N). Because we use inorder traversal.
Space complexity: O(N). For stack may contains all the nodes.
"""

"""
For follow up question.
We might need to keep a sorted list of node.
Every time we inset and delete. We need to update the list. Taking up O(N) of time.
(Originally it was O(LogN) for insert and delete)
But to find the kth smallest element will only takes O(1).
"""