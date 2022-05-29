from collections import deque

class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
        
        q = deque()
        q.append((root.left, root.right))
        while q:
            left_node, right_node = q.popleft()
            if not left_node and right_node: return False
            if not right_node and left_node: return False
            
            if left_node and right_node:
                if left_node.val!=right_node.val: return False
                q.append((left_node.right, right_node.left))
                q.append((left_node.left, right_node.right))
        return True


# class Solution(object):
#     def isSymmetric(self, root):
#         if not root: return True
        
#         stack = []
#         stack.append((root.left, root.right))
#         while stack:
#             left_node, right_node = stack.pop()
#             if not left_node and right_node: return False
#             if not right_node and left_node: return False
            
#             if left_node and right_node:
#                 if left_node.val!=right_node.val: return False
#                 stack.append((left_node.right, right_node.left))
#                 stack.append((left_node.left, right_node.right))
#         return True

"""
Time: O(N)
Space: O(N)

Use 2 DFS to traverse the tree at the same time.
s1 will go left first.
s2 will fo right first.
Make sure every element popping out is the same.
"""
class Solution(object):
    def isSymmetric(self, root):
        s1 = [root]
        s2 = [root]
        
        while s1 and s2:
            node1 = s1.pop()
            node2 = s2.pop()
            
            if not node1 and not node2: continue
            if not node1 and node2: return False
            if node1 and not node2: return False
            if node1.val!=node2.val: return False
            
            s1.append(node1.left)
            s1.append(node1.right)
            s2.append(node2.right)                
            s2.append(node2.left)
        
        if s1 or s2: return False #if there are something left in one of the stack
        return True