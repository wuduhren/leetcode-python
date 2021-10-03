"""
Time: O(H), since we are just moving vertically in the tree.
Space: O(1)

First, check if the node has right child, if so, continue the traversal.
If the node doesn't have right child, this mean that the node and all its children are visited.
We need to move up.
While moving up a node, if a node itself is a right child, we need to keep moving up, since the node's parent is already vistied.
Keep moving up until the node itself is a left child. Return its parent.
"""
class Solution(object):
    def inorderSuccessor(self, node):
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node.parent.right==node:
            node = node.parent
        return node.parent