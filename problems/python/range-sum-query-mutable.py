"""
Time: O(LogN) for all operations.
Space: O(N) for the segment tree.

Build a segment tree from the array `nums`. Each node store the info of the segment in nums (from `node.start` to `node.end`)
And `node.val` is equal to sum from nums[start] to nums[end]
"""
class NumArray(object):

    def __init__(self, nums):
        def buildSegmentTree(start, end):
            if start>end: return None
            node = Node(start, end)
            
            if start==end:
                node.val = nums[end]
            else:
                node.left = buildSegmentTree(start, node.mid)
                node.right = buildSegmentTree(node.mid+1, end)
                node.val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            
            return node
        
        self.root = buildSegmentTree(0, len(nums)-1)
        
        
    def update(self, i, val):
        def helper(node, i, val):
            if node.start==node.end==i:
                node.val = val
                return
            
            if node.mid<i:
                helper(node.right, i, val)
            elif i<=node.mid:
                helper(node.left, i, val)
            node.val = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            
        return helper(self.root, i, val)
                
        

    def sumRange(self, i, j):
        def helper(node, i, j):
            if not node: return 0
            if node.start==i and node.end==j:
                return node.val
            elif node.mid<i:
                return helper(node.right, i, j)
            elif j<=node.mid:
                return helper(node.left, i, j)
            else:
                return helper(node.left, i, node.mid)+helper(node.right, node.mid+1, j)
        return helper(self.root, i, j)
        


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.mid = (start+end)/2
        self.val = 0
        
        self.left = None
        self.right = None
        