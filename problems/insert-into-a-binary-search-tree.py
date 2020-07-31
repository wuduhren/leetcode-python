class Solution(object):
    def insertIntoBST(self, root, val):
        if not root: return TreeNode(val)
        
        node = root
        while node:
            if val<node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
        
        return None


"""
Time complexity: O(LogN)
Space complexity: O(1)
"""