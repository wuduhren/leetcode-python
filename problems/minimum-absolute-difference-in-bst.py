class Solution(object):
    def getMinimumDifference(self, root):
        stack = []
        node = root
        temp = float('-inf')
        ans = float('inf')
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            ans = min(ans, node.val-temp)
            temp = node.val
            
            node = node.right
        return ans

"""
Time complexity: O(N)
Space complexity: O(1)
"""


class Solution(object):
    def getMinimumDifference(self, root):
        def traverse(node):
            if not node: return
            traverse(node.left)
            A.append(node.val)
            traverse(node.right)
            
        A = []
        ans = float('inf')
        traverse(root)
        
        for i, n in enumerate(A):
            if i==0: continue
            ans = min(ans, A[i]-A[i-1])
        return ans

"""
Time complexity: O(N)
Space complexity: O(N)
"""