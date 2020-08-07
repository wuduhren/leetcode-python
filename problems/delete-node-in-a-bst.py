class Solution(object):
    def deleteNode(self, root, key):
        def find_min(root):
            curr = root
            while curr.left: curr = curr.left
            return curr.val#[5]
        
        def remove(node):
            if node.left and node.right:
                node.val = find_min(node.right)
                node.right = self.deleteNode(node.right, node.val)
                return node #[4]
            elif node.left and not node.right:
                return node.left #[3]
            elif node.right and not node.left:
                return node.right #[3]
            else:
                return None #[2]
            
        if not root: return root
        node = root
        
        while node: #[0]
            if node.val==key:
                return remove(node) #[1]
            elif node.left and node.left.val==key:
                node.left = remove(node.left) #[1]
                return root
            elif node.right and node.right.val==key:
                node.right = remove(node.right) #[1]
                return root
            
            if key>node.val and node.right:
                node = node.right
            elif key<node.val and node.left:
                node = node.left
            else:
                break
                
        return root

"""
Find the parant and the node to be deleted. [0]
Deleting the node means replacing its reference by something else. [1]

For the node to be deleted, if it only has no child, just remove it from the parent. Return None. [2]

If it has one child, return the child. So its parent will directly connect to its child. [3]

If it has both child. Update the node's val to the minimum value in the right subtree. Remove the minimum value node in the right subtree. [4]
This is equivalent to replacing the node by the minimum value node in the right subtree.
Another option is to replace the node by the maximum value node in the left subtree.

Find the minimum value in the left subtree is easy. The leftest node value in the tree is the smallest. [5]

Time Complexity: O(LogN). O(LogN) for finding the node to be deleted.
The recursive call in `remove()` will be apply to a much smaller subtree. And much smaller subtree...
So can be ignored.
Space complexity is O(LogN). Because the recursive call will at most be called LogN times.
N is the number of nodes. And LogN can be consider the height of the tree.
"""