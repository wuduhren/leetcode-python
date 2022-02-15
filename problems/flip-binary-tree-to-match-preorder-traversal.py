class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        def helper(node):
            if not node: return
            if node.val!=voyage[self.i]:
                self.valid = False
                return
            
            self.i += 1
            if node.left and node.left.val!=voyage[self.i]:
                self.ans.append(node.val)
                helper(node.right)
                helper(node.left)
                
            else:
                helper(node.left)
                helper(node.right)
        
        self.ans = []
        self.i = 0
        self.valid = True
        helper(root)
        return self.ans if self.valid else [-1]