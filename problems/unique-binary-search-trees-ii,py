class Solution(object):
    def generateTrees(self, N):
        
        #generateTrees from s to e
        def helper(s, e):
            trees = []
            
            for i in xrange(s, e+1):
                leftTrees = helper(s, i-1)
                rightTrees = helper(i+1, e)
                
                for leftTree in leftTrees:
                    for rightTree in rightTrees:
                        
                        root = TreeNode(i)
                        root.left = leftTree
                        root.right = rightTree
                        trees.append(root)
            
            return trees if trees else [None]
        
        #remove None in the output
        return [tree for tree in helper(1, N) if tree]