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