"""
1.
for recursive/iterative solution
if you are a left node
your max will be your parent's value
your min will be yout parent's min, because your parent might be someone's right child.

if you are a right node
your min will be your parent's value
your max will be your parent's max, because your parent might be someone's left child.

root have no max and min

2.
for in-order traversal solution
if you use in-order to traverse a BST
the value you list out will be in order(sorted)
so each element would be greater than the last one

in-order traverse:
left child -> current node -> right child

normaly I will recursivly do the in-order traversing
but iterative is easier to track the last element'value

3. I personally like in-order traversal solution
"""
class Solution(object):
	#recursive
    def isValidBST(self, root):
        def helper(node, min_val, max_val):
            if not node: return True
            if node.val<=min_val or node.val>=max_val:return False
            if not helper(node.left, min_val, node.val): return False
            if not helper(node.right, node.val, max_val): return False
            return True
        return helper(root, float('-inf'), float('inf'))

    #iterative
    def isValidBST(self, root):
        if root==None: return True
        stack = [(root, float('-inf'), float('inf'))]
        while stack:
            node, min_val, max_val = stack.pop()
            if node.val<=min_val or node.val>=max_val:
                return False
            if node.left:
                stack.append((node.left, min_val, node.val))
            if node.right:
                stack.append((node.right, node.val, max_val))
        return True
   	        
    #in-order traversal
    def isValidBST(self, root):
        stack = []
        last_val = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if root.val<=last_val:
                return False
            
            last_val = root.val
            root = root.right #if root.right: root = root.right
        return True
