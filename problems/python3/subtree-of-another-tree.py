class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot: return root==subRoot
        if self.isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSame(self, p, q):
        if not p or not q: return p==q
        if p.val!=q.val: return False
        return self.isSame(p.left, q.left) and self.isSame(p.right, q.right)