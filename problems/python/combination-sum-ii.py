"""
If you haven't see the [first problem](https://leetcode.com/problems/combination-sum/) and [explanation](https://leetcode.com/problems/combination-sum/discuss/386093/) already, I suggest you check it out first.

This Problem is similar to the [first one](https://leetcode.com/problems/combination-sum/).
Except that we can only select each element in the `candidates` once.
In the first problem, we can choose the same element in the `candidates` for many times as we like.
In this problem, we can't.
So we need to
```
helper(combination+[num], i+1, target_remain-num)
```
Instead of
```
helper(combination+[num], i, target_remain-num)
```

Another problem is duplicates. For example,
```
candidates = [10,1,2,7,6,1,5]
target = 8
```
We might end up choosing the fist 1 or second 1 and make the same combination `[1, 2, 5]`
So I use a hash set to prevent duplicate.
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        def helper(combination, start, target_remain):
            if target_remain==0:
                answer.add(tuple(combination))
            for i in xrange(start, len(candidates)):
                num = candidates[i]
                if num>target_remain: break
                helper(combination+[num], i+1, target_remain-num)

        answer = set()
        candidates.sort()
        helper([], 0, target)
        return [list(combination) for combination in answer]

#DFS
class Solution(object):
    def combinationSum2(self, candidates, T):
        def dfs(index, target, path):
            if target<0:
                return
            elif target==0:
                opt.append(path)
            else:
                for i in xrange(index, len(candidates)):
                    if i>index and candidates[i]==candidates[i-1]: continue
                    num = candidates[i]
                    dfs(i+1, target-num, path+[num])
        opt = []
        candidates.sort()
        dfs(0, T, [])
        return opt


class Solution(object):
    def combinationSum2(self, candidates, target):
        def helper(remain, comb, start):
            if remain==0:
                ans.append(comb[:])
            elif remain<0:
                return
            else:
                for i in xrange(start, len(candidates)):
                    if i>start and candidates[i]==candidates[i-1]: continue
                    candidate = candidates[i]
                    comb.append(candidate)
                    helper(remain-candidate, comb, i+1)
                    comb.pop()
        
        ans = []
        candidates.sort()
        helper(target, [], 0)
        return ans
        
        
                    