#https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
class Solution(object):
    def treeToDoublyList(self, root):
        
        #the helper gets you an sorted double link list that originally start at node
        #if you put a node's left to the helper, it will need to return the right most node of the sorted link list
        #if you put a node's right to the helper, it will need to return the left most node of the sorted link list
        #so we use hook_left to control returning right most or left most
        def helper(node, hook_left=True):
            if node is None: return None
            node.left = helper(node.left)
            node.right = helper(node.right, False)
            
            if node.left:
                node.left.right = node
            if node.right:
                node.right.left = node
                
            if hook_left:
                while node.right:
                    node = node.right
            else:
                while node.left:
                    node = node.left
                    
            return node
        
        
        if root is None: return None
        
        #get the right most before sorted(the right most is still right most after sorted)
        #we need this to link the left most after sorting
		#we do this before sorting because, it is faster to find the right most in the tree
        right_most = root
        while right_most.right:
            right_most = right_most.right
        
        #get the sorted double link list that originally start at root
        #set hook_left to False, so it will return the left most (head)
        root = helper(root, False)
        
        #linked two end together
        root.left = right_most
        right_most.right = root
        
        return root





"""
Time: O(N)
Space: O(LogN) if the tree is balanced.

Do an inorder traversal and link the node.left to the prev and prev.right to node.
"""
class Solution(object):
    def treeToDoublyList(self, root):
        if not root: return root
        
        stack = []
        node = root
        preHead = Node(-1)
        prev = preHead
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            prev.right = node
            node.left = prev
            
            prev = node
            
            node = node.right
        
        head = preHead.right
        head.left = prev
        prev.right = head
        
        return head

"""
FYI
"""
def inOrderTraverse(root):
    stack = []
    node = root
    
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        #do something
        print node.val
        
        node = node.right