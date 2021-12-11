"""
Time complexity: O(LogN)
Space complexity: O(1)
"""
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
Space complexity: O(LogN)
"""
class Solution(object):
    def insertIntoBST(self, root, val):
        def helper(node, val):
            if not node: return
            if val<node.val:
                if node.left:
                    helper(node.left, val)
                else:
                    node.left = TreeNode(val)
            else:
                if node.right:
                    helper(node.right, val)
                else:
                    node.right = TreeNode(val)
        
        if not root: return TreeNode(val)
        helper(root, val)
        return root
        