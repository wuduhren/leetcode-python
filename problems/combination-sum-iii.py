"""
If you haven't seen [this problem](https://leetcode.com/problems/combinations/), I suggest you do that first!
And here is the [explaination](https://leetcode.com/problems/combinations/discuss/387753) for that problem.

This problem is basically the same as [that problem](https://leetcode.com/problems/combinations/) with its N=9.
The difference is we have to find the combination that sum up as N.
So all we have to do is change the condition of [0]. And the condition for backtracking [1].
"""
class Solution(object):
    def combinationSum3(self, K, N):
        answer = []
        ans = []
        first = 1
        total = 0
        while True:
            if len(ans)==K and total==N: #[0]
                answer.append(ans[:])

            if len(ans)==K or total>N or first>9: #[1]
                if not ans: return answer
                first = ans.pop() #backtrack
                total-=first
                first+=1
            else:
                ans.append(first)
                total+=first
                first+=1

#DFS
class Solution(object):
    def combinationSum3(self, K, N):
        def dfs(path, min_num):
            if len(path)==K and sum(path)==N:
                opt.append(path)
            for num in xrange(min_num, 10):
                dfs(path+[num], num+1)
        opt = []
        dfs([], 1)
        return opt

