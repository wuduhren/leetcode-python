from collections import Counter
class Solution(object):
    def findMode(self, root):
        def count(node):
            counter[node.val] += 1
            if node.left: count(node.left)
            if node.right: count(node.right)
        
        if not root: return []
        
        counter = Counter()
        count(root)
        max_count = max(counter.values())
        return [val for val, count in counter.items() if count==max_count]

"""
Time: O(N). For we traverse every node recursively.
Space: O(N). Becuase we store all element's val and count in `counter`.
Note that, we do not use the feature of BST.
"""

class Solution(object):
    def findMode(self, root):
        if not root: return []
        
        ans = []
        stack = []
        prev_val = None
        curr = root
        curr_count = 0
        max_count = float('-inf')
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            #[0]
            if curr.val!=prev_val:
                curr_count = 1
                prev_val = curr.val
            else:
                curr_count += 1
            
            #[1]
            if curr_count>max_count:
                ans = [curr.val]
                max_count = curr_count
            elif curr_count==max_count:
                ans.append(curr.val)
            
            curr = curr.right
                
        return ans

"""
To use the feature of BST, we are going to inorder traverse the BST.
So it will be like we are iterating a sorted array.

[1]
While iterating, we can put only the element count that is greater or equal than `max_count` to `ans`.
If we encounter a new element with larger `curr_count`, we reset the `ans`.

[0]
With the help of `prev_val` we can know that `curr_node` is the same to the previous or not.
If not, its a new element, we need to reset the `curr_count`.

Time: O(N). Space: O(LogN)

For better understanding, below is a template for inorder traverse.
"""

#inorder traversal of BST
def inorder_traverse(root):
    curr = root
    stack = []
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        
        #do something to the current node
        print curr.val
        
        curr = curr.right
