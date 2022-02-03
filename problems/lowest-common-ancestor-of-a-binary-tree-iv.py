class Solution(object):
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root, nodes):
        def dfs(node):
            if not node: return 0
            
            count = 0
            if node in nodes: count += 1
            count += dfs(node.left)
            count += dfs(node.right)
            if count>=len(nodes) and not self.ans: self.ans = node    
            return count
        
        nodes = set(nodes)
        dfs(root)
        return self.ans