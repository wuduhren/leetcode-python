"""
the `helper()` check if the `target_remain` is 0.
If true, it means that the sum of `combination` is equal to the `target`. Put the `combination` to the `answer`.
If not, we For-loop each number, put it in the `combination` and try the `combination`. See if the number can make `target_remain` 0.


The `start` means the `candidates[start:]` are the candidate we only need to concider.
For example if
```
candidates = [2,3,6,7], target = 7
```
If we pick 3, we are not allow to pick 2 any more, or we will have duplicate combination.
We are only allow to pick the number at the same index or afterwards.


So in the For-loop, if the smallest candidate is larger than the `target_remain`, we don't need to check afterwards.
And that is why we need to sort the `candidates` in the first place.

```
candidates = [2,3,6,7]
target = 7

helper([], 0, 7)
    helper([2], 0, 5)
        helper([2, 2], 0, 3)
            helper([2, 2, 2], 0, 1)
            BREAK. When we are about to call helper([2, 2, 2, 2], 0, 1), we found that 2>target_remain.

            helper([2, 2, 3], 1, 0) --> bingo

        helper([2, 3], 1, 2)
        BREAK. When we are about to call helper([2, 6], 2, 2), we found that 6>target_remain.

    helper([3], 1, 4)
        .
        .
        .

    helper([6], 2, 1)
        .
        .
        .

    helper([7], 3, 0) --> bingo
```
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        def helper(combination, start, target_remain):
            if target_remain==0:
                answer.append(combination)
            for i in xrange(start, len(candidates)):
                num = candidates[i] #try out if with num adding into combination can make target_remain 0
                if num>target_remain: break
                helper(combination+[num], i, target_remain-num)

        candidates.sort()
        answer = []
        helper([], 0, target)
        return answer



#Old Solution
class Solution(object):
    def combinationSum(self, candidates, target):
        def helper(candidates, target, combination):
            if not candidates: return []
            n = candidates[0]
            if n>target:
                return []
            elif n==target:
                return [combination+[n]]
            else:
                return helper(candidates, target-n, combination+[n]) + helper(candidates[1:], target, combination)
        return helper(sorted(candidates), target, [])


# 2019/9/12 Update
class Solution(object):
    def combinationSum(self, candidates, T):
        answer = []
        ans = []
        first = 0
        total = 0

        candidates.sort()

        memo = {}
        for i, num in enumerate(candidates):
            memo[num] = i

        while True:
            if total==T:
                answer.append(ans[:])
            if total>=T or first>=len(candidates):
                if not ans: return answer
                num = ans.pop()
                first = memo[num]+1
                total-=num
            else:
                ans.append(candidates[first])
                total+=candidates[first]

# DFS
class Solution(object):
    def combinationSum(self, candidates, T):
        def dfs(index, target, path):
            if target<0:
                return
            elif target==0:
                opt.append(path)
            else:
                for i in xrange(index, len(candidates)):
                    num = candidates[i]
                    dfs(i, target-num, path+[num])
        opt = []
        candidates.sort()
        dfs(0, T, [])
        return opt


"""
Time: O(N^(T/M)), N is the number of candidates. T is target. M is min(candidates).
Space: O(T/M)
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        def helper(remain, comb, start=0):
            if remain==0:
                ans.append(comb[:])
            elif remain<0:
                return
            elif remain>0:
                for i in xrange(start, len(candidates)):
                    candidate = candidates[i]
                    comb.append(candidate)
                    helper(remain-candidate, comb, i)
                    comb.pop()
        
        ans = []
        helper(target, [])
        return ans