class Solution(object):
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root, p, q):
        def dfs(node):
            if not node: return 0
            
            count = 0
            if node is p or node is q: count += 1
            count += dfs(node.left)
            count += dfs(node.right)
            if count>=2 and not self.ans: self.ans = node
            return count
        
        dfs(root)
        return self.ans
