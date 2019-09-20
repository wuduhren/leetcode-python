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
                n = candidates[i]
                if n>target_remain: break
                helper(combination+[n], i, target_remain-n)

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
