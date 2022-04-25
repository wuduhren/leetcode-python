class Solution(object):
    def findDuplicateSubtrees(self, root):
        def dfs(node):
            if not node: return '#'
            string = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
            data[string].append(node)
            return string
        
        data = collections.defaultdict(list)
        ans = []
        
        dfs(root)
        
        for s in data:
            if len(data[s])>=2: ans.append(data[s][0])
        return ans