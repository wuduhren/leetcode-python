from collections import Counter
class Solution(object):
    def findFrequentTreeSum(self, root):
        def dfs(node):
            if not node: return 0
            s = dfs(node.left)+node.val+dfs(node.right)
            counter[s] += 1
            return s
        
        if not root: return []
        counter = Counter()
        dfs(root) #start counting

        max_freq = max(counter.values())
        return [v for v, freq in counter.items() if freq==max_freq]

"""
Time: O(N)
Space: O(N)
"""