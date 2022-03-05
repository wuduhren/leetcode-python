class Solution(object):
    def addOperators(self, num, target):
        def dfs(num, curr, i):
            if i==len(num):
                if eval(curr[1:])==target: ans.append(curr[1:])
                return
            
            if curr and curr[-1] in operators:
                dfs(num, curr+num[i], i+1)
            elif curr and curr[-1]=='0':
                dfs(num, curr+'+', i)
                dfs(num, curr+'-', i)
                dfs(num, curr+'*', i)
            else:
                dfs(num, curr+'+', i)
                dfs(num, curr+'-', i)
                dfs(num, curr+'*', i)
                dfs(num, curr+num[i], i+1)
        
        operators = set(['+', '-', '*'])
        ans = []
        dfs(num, '+', 0)
        return ans