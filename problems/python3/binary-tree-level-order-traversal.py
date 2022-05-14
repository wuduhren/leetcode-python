"""
Time: O(N), since we need to go through all the nodes.
Space: O(LogN) for recursion stack. (if the tree is balanced). This do not take the output into account.
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, level):
            if not node: return
            if level==len(ans): ans.append([])
            ans[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        
        ans = []
        helper(root, 0)
        
        return ans


"""
Time: O(N), since we need to go through all the nodes.
Space: O(N) for queue.
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        q = collections.deque([(root, 0)])
        ans = []
        
        while q:
            node, level = q.popleft()
            
            if level==len(ans): ans.append([])
            ans[level].append(node.val)
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        
        return ans