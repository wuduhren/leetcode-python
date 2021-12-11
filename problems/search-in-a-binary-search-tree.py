"""
Time complexity: O(LogN)
Space complexity: O(1)
"""
class Solution(object):
    def searchBST(self, root, val):
        node = root
        
        while node:
            if node.val==val:
                return node
            elif node.val>val:
                node = node.left
            else:
                node = node.right

        return None

"""
Time complexity: O(LogN)
Space complexity: O(LogN)
"""
class Solution(object):
    def searchBST(self, node, val):
        if not node: return None
        if node.val==val:
            return node
        elif node.val<val:
            return self.searchBST(node.right, val)
        elif node.val>val:
            return self.searchBST(node.left, val)