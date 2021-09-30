"""
Time: O(LogN)
Space: O(1)

Basically we are going to search the target in the BST.
Along the way, we compare it with the `ans`, if the difference is smaller, update it.
"""
class Solution(object):
    def closestValue(self, root, target):
        node = root
        ans = float('inf')
        
        while node:
            if not node: break
            
            if abs(ans-target)>abs(node.val-target):
                ans = node.val
            
            if target>node.val:
                node = node.right
            else:
                node = node.left
                
        return ans