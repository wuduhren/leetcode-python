class Solution(object):
    def __init__(self):
        self.ans = None
        
    def lcaDeepestLeaves(self, root):
        def checkCount(node, deepestNode):
            if not node:
                count = 0
                if count==len(deepestNode) and not self.ans: self.ans = node
                return 0
            
            if node in deepestNode:
                count = 1
                if count==len(deepestNode) and not self.ans: self.ans = node
                return count
            
            leftCount = checkCount(node.left, deepestNode)
            rightCount = checkCount(node.right, deepestNode)
            
            if leftCount+rightCount==len(deepestNode) and not self.ans: self.ans = node
            return leftCount+rightCount
            
        q = collections.deque([(root, 0)])
        q2 = collections.deque()
        deepestNode = set([node for node, h in q])
        
        while q:
            node, d = q.popleft()
            if node.left: q2.append((node.left, d+1))
            if node.right: q2.append((node.right, d+1))
            if not q:
                q = q2
                if q: deepestNode = set([node for node, h in q])
                q2 = collections.deque()
        
        checkCount(root, deepestNode)
        return self.ans
        
                
            
        