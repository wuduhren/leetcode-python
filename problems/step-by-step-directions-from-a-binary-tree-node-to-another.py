class Solution(object):
    def __init__(self):
        self.lca = None
        
    def getDirections(self, root, startValue, destValue):
        def findPath(node, path, val):
            if not node: return False
            if node.val==val: return True
            
            path.append('L')
            if findPath(node.left, path, val): return True
            path.pop()
            
            path.append('R')
            if findPath(node.right, path, val): return True
            path.pop()
            
            return False
            
        def findCount(node, startValue, destValue):
            if not node: return 0
            count = 0
            if node.val==startValue or node.val==destValue: count += 1
            count += findCount(node.left, startValue, destValue)
            count += findCount(node.right, startValue, destValue)
            if count>=2 and not self.lca: self.lca = node
            return count
        
        findCount(root, startValue, destValue)
        
        path1 = []
        findPath(self.lca, path1, startValue)
        path2 = []
        findPath(self.lca, path2, destValue)
        
        return 'U'*len(path1) + ''.join(path2)