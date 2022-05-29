"""
Time: O(N)
Space: O(N)

Traverse the tree level by level.
For each level connect the node to the "next node".
"""
class Solution(object):
    def connect(self, root):
        if not root: return root
        level = collections.deque([root])
        nextLevel = collections.deque()
        
        while level:
            node = level.popleft()
            
            if node.left: nextLevel.append(node.left)
            if node.right: nextLevel.append(node.right)
            
            if not level:
                if not nextLevel: break
                for i, c in enumerate(nextLevel):
                    if i==len(nextLevel)-1: continue #skip last
                    c.next = nextLevel[i+1]
                level = nextLevel
                nextLevel = collections.deque()
                
        return root


"""
Time: O(N)
Space: O(1)

View each level as a link list.
Traverse the tree level by level. For each level:
Starting from the leftmost (the head of the link list), we establish the next pointer of the children.
curr.left.next = curr.right
curr.right.next = curr.next.left
"""
class Solution(object):
    def connect(self, root):
        if not root: return root
        
        leftmost = root
        while leftmost:
            
            curr = leftmost
            while curr:
                if curr.left: curr.left.next = curr.right
                if curr.right and curr.next: curr.right.next = curr.next.left
                curr = curr.next
                
            leftmost = leftmost.left
        
        return root