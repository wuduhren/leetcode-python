"""
The description wants us to report from left to right, top to bottom.
Thus, we keep add value into `temp` with `x_position` as the key and `(y_position, node.val)` as the value.
And maintain `min_x`, `max_x` at the same time. So we know how to iterate the `temp`.
"""
from collections import defaultdict

class Solution(object):
    def verticalTraversal(self, root):
        temp = defaultdict(list)
        min_x = 0
        max_x = 0

        stack = []
        stack.append((root, 0, 0))
        while stack:
            node, x, y = stack.pop()
            temp[x].append((y, node.val)) #append the value of height, so we can sort by height later on
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            if node.left: stack.append((node.left, x-1, y+1))
            if node.right: stack.append((node.right, x+1, y+1))
        
        opt = []
        for i in range(min_x, max_x+1):
            opt.append([v for y, v in sorted(temp[i])]) #the temp[i] will be sorted by y_position then sorted by node.val
        
        return opt