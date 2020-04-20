class Solution(object):
    def sumNumbers(self, root):
        if not root: return 0
        ans = 0
        stack = []
        stack.append((root, ''))
        
        while stack:
            node, total = stack.pop()
            total += str(node.val)
            if not node.left and not node.right: #is_leaf
                ans += int(total)
                continue
            if node.left:
                stack.append((node.left, total))
            if node.right:
                stack.append((node.right, total))
        return ans

"""
Time complexity: O(N), since we use DFS to traverse each node once.
Space complexity: O(NLogN), since each node (at the very bottom), may carry all the digit from its ancestor, LogN.
"""