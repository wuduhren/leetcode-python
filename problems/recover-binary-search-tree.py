"""
Time: O(NLogN)
Space: O(N)
"""
class Solution(object):
    def recoverTree(self, root):
        memo = {} #{node.val:node}
        stack = []
        node = root
        vals = []
        
        #inorder traversal and store the values in `vals` and `memo`
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            memo[node.val] = node
            vals.append(node.val)
            
            node = node.right
        
        #find two val that needed to be swapped
        diff = []
        sortedVals = sorted(vals)
        for i in xrange(len(sortedVals)):
            if vals[i]!=sortedVals[i]: diff.append(vals[i])
            if len(diff)>=2: break
        
        #swap the values
        memo[diff[0]].val = diff[1]
        memo[diff[1]].val = diff[0]
        
        return root


"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def recoverTree(self, root):
        stack = []
        node = root
        prev = TreeNode(float('-inf'))
        swap1 = swap2 = None
        
        #inorder traversal and find the swapped values
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            if swap1==None and prev.val>node.val: swap1 = prev
            if swap1!=None and prev.val>node.val: swap2 = node

            prev = node

            node = node.right
        
        #swap the values
        swap1.val, swap2.val = swap2.val, swap1.val
        
        return root