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
Space complexity: O(1)
"""