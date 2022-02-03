class Solution(object):
    def __init__(self):
        self.lca = None
        self.pHeight = 0
        self.qHeight = 0
        
    def findDistance(self, root, p, q):
        #find the count of p or q in node's subtree, set the first node we found that has count>=2 as lca.
        def findCount(node):
            if not node: return 0
            count = 0
            if node.val==p or node.val==q: count += 1
            count += findPQCount(node.left)
            count += findPQCount(node.right)
            if count>=2 and not self.lca: self.lca = node
            return count
        
        def findHeight(node, h):
            if not node: return
            if node.val==p: self.pHeight = h
            if node.val==q: self.qHeight = h
            if self.pHeight and self.qHeight: return
            findHeight(node.left, h+1)
            findHeight(node.right, h+1)
            
        findCount(root)
        findHeight(self.lca, 0)
        return self.qHeight + self.pHeight