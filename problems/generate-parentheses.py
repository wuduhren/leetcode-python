"""
If we need `N` pairs of parentheses, we need to use `N` open parenthesis (`open_remain`) and `N` close parenthesis (`close_remain`).
We use `dfs()` to explore all kinds of possiblities.
`open_count` keeps track of how many open parenthesis is in the `path` now. Because number of close parenthesis may not exceed open parenthesis in any given point.

The time complexity is O(2^N), since we can roughly see every position has two options, open or close.
The space complexity is O(2^N), too. And the recuresion level is O(N).
"""
class Solution(object):
    def generateParenthesis(self, N):
        def dfs(path, open_count, open_remain, close_remain):
            if open_remain==0 and close_remain==0:
                opt.append(path)
                return
            if open_count>0 and close_remain>0:
                dfs(path+')', open_count-1, open_remain, close_remain-1)
            if open_remain>0:
                dfs(path+'(', open_count+1, open_remain-1, close_remain)

        opt = []
        dfs('', 0, N, N)
        return opt


class Solution(object):
    def generateParenthesis(self, N):
        def helper(open_remain, close_remain, s):
            if open_remain==0 and close_remain==0:
                ans.append(s)
            if close_remain>open_remain and close_remain>0:
                helper(open_remain, close_remain-1, s+')')
            if open_remain>0:
                helper(open_remain-1, close_remain, s+'(')
        ans = []
        helper(N, N, '')
        return ans

"""
Time: O(2^N)
Space: O(N)
"""
class Solution(object):
    def generateParenthesis(self, n):
        def helper(curr, openCount, left, right):
            if left==0 and right==0: ans.append(curr)
            if left>0:
                helper(curr+'(', openCount+1, left-1, right)
            if right>0 and openCount>0:
                helper(curr+')', openCount-1, left, right-1)
        
        ans = []
        helper('', 0, n, n)
        return ans