"""
Time: O(N), each nodes is traversed 2 times.
Space: O(N) for `parents` and `q`, `ans`, `ans2`

[1]
Through BFS
Store the parent of each node in the `parents`.
Also store the leaf node in the `temp`.

[2]
Store the `temp` to the ans.
For each node stored to the ans, we need to "detach" it from its parent.
Also check if the parent become a leaf node, if so, store it in the new `temp`.

[3]
Store the val from node reference in ans to ans2.
"""
class Solution(object):
    def findLeaves(self, root):
        ans = []
        q = collections.deque([root])
        parents = {}
        
        #[1]
        temp = []
        while q:
            node = q.popleft()
            
            if not node.left and not node.right:
                temp.append(node)
            
            if node.left:
                q.append(node.left)
                parents[node.left] = node
            
            if node.right:
                q.append(node.right)
                parents[node.right] = node

        #[2] 
        while temp:
            ans.append(temp)
            temp = []
            
            for node in ans[-1]:
                if node not in parents: break
                p = parents[node]
                if p.left==node: p.left = None
                if p.right==node: p.right = None
                if not p.left and not p.right: temp.append(p)
        
        #[3]
        ans2 = []
        for temp in ans:
            ans2.append([node.val for node in temp])
        
        return ans2