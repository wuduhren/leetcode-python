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

#2020/7/11
class Solution(object):
    def sumNumbers(self, root):
        if not root: return 0

        ans = 0
        stack = []
        stack.append((root, 0))

        while stack:
            node, n = stack.pop()
            n = n*10+node.val
            if not node.left and not node.right: ans+=n
            if node.left: stack.append((node.left, n))
            if node.right: stack.append((node.right, n))

        return ans

"""
Time complexity: O(N), since we use DFS to traverse each node once.
Space complexity: O(LogN).
Most of the memory we use is in the stack.
tack will at most carry one path (root to leaf), each node containing one digit. O(LogN)
"""















