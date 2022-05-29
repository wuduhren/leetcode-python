class Solution(object):
    def pruneTree(self, root):
        def hasOne(node):
            if not node: return False

            left_has_one = hasOne(node.left)
            right_has_one = hasOne(node.right)

            if not left_has_one: node.left = None
            if not right_has_one: node.right = None

            return node.val==1 or left_has_one or right_has_one
        
        return root if hasOne(root) else None

class Solution(object):
    def pruneTree(self, node):
        if not node: return None
        node.left = self.pruneTree(node.left)
        node.right = self.pruneTree(node.right)
        if not node.left and not node.right and node.val==0: return None
        return node

"""
Time complexity is O(N). Because we traverse all the nodes.
Space complexity is O(N). In the worst case, the recursion will go O(N) level deep.
"""