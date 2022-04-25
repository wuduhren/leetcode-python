"""
1.
for recursive/iterative solution
if you are a left node
your max will be your parent's value
your min will be yout parent's min, because your parent might be someone's right child.

if you are a right node
your min will be your parent's value
your max will be your parent's max, because your parent might be someone's left child.

node have no max and min

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
    def isValidBST(self, node):
        def helper(node, min_val, max_val):
            if not node: return True
            if node.val<=min_val or node.val>=max_val:return False
            if not helper(node.left, min_val, node.val): return False
            if not helper(node.right, node.val, max_val): return False
            return True
        return helper(node, float('-inf'), float('inf'))

    #iterative
    def isValidBST(self, node):
        if node==None: return True
        stack = [(node, float('-inf'), float('inf'))]
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
    def isValidBST(self, node):
        stack = []
        last_val = float('-inf')
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if node.val<=last_val:
                return False
            
            last_val = node.val
            node = node.right #if node.right: node = node.right
        return True



#2021/9/14
"""
Time: O(N)
Space: O(N)

Use in-order traversal to check. If the bst is valid, the node.val should always be larger than the prev.
"""
class Solution(object):
    def isValidBST(self, root):
        node = root
        stack = []
        prev = float('-inf')
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            if prev>=node.val: return False
            prev = node.val
            
            node = node.right
            
        return True