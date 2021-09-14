class Solution(object):
    def pathSum(self, root, S):
        if not root: return False
        
        opt = []
        stack = []
        stack.append((root, 0, []))
        
        while stack:
            node, s, path = stack.pop()
            s += node.val
            path = path + [node.val]
            if not node.left and not node.right and s==S: opt.append(path)
            if node.left: stack.append((node.left, s, path))
            if node.right: stack.append((node.right, s, path))
        return opt
"""
Time complexity is O(N), because we traverse all the nodes.
Space complexity is O(N^2), because in the worst case, all node could carry all the other nodes in the `path`.
"""



"""
Time complexity is O(N), because we traverse all the nodes.
Space complexity is O(N^2), because in the worst case, all node could carry all the other nodes in the `path`.
"""
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root: return []
        
        ans = []
        stack = [(root, root.val, [root.val])]
        
        while stack:
            node, total, path = stack.pop()
            
            if not node.left and not node.right and total==targetSum: ans.append(path)
            if node.left: stack.append((node.left, total+node.left.val, path+[node.left.val]))
            if node.right: stack.append((node.right, total+node.right.val, path+[node.right.val]))
                
        return ans