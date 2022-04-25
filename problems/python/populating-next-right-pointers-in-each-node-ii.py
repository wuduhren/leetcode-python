"""
Time: O(N)
Space: O(1)

View each level as a link list.
Traverse the tree level by level. For each level:
Starting from the leftmost (the head of the link list), we establish the next pointer of the children.

curr.left.next = curr.right or (curr.next.left or curr.next.right) or (curr.next.next.left or curr.next.next.right) or (...)
curr.right.next = (curr.next.left or curr.next.right) or (curr.next.next.left or curr.next.next.right) or (...)
"""
class Solution(object):
    def connect(self, root):
        if not root: return root
        
        leftmost = root
        
        while leftmost:
            curr = leftmost
            
            while curr:
                if curr.left:
                    if curr.right:
                        curr.left.next = curr.right
                    else:
                        n = curr.next
                        while n:
                            curr.left.next = n.left or n.right
                            if curr.left.next: break
                            n = n.next
                
                if curr.right:
                    n = curr.next
                    while n:
                        curr.right.next = n.left or n.right
                        if curr.right.next: break
                        n = n.next
                
                curr = curr.next
            
            nextLevelLeftmost = None
            n = leftmost
            while n:
                if n.left or n.right:
                    nextLevelLeftmost = n.left or n.right
                    break
                n = n.next
            leftmost = nextLevelLeftmost
            
        return root