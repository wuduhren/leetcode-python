"""
For every number in `nums` you either take (O) or not take it (X).
So for example
```
nums = [1,2,3]

Subset [] is [X,X,X]
Subset [1] is [O,X,X] => [1,X,X]
Subset [2] is [X,O,X] => [X,2,X]
Subset [3] is [X,X,O] => [X,X,3]
Subset [1,2] is [O,O,X] => [1,2,X]
Subset [1,3] is [O,X,O] => [1,X,3]
.
.
.

Subset [1,2,3] is [O,O,O] => [1,2,3]
```
So there are total 2x2x2 posibilities (subsets).
Because for each number, it has two choices, take (O) or not take (X).
"""


class Solution(object):
    def subsets(self, nums):
        def helper(i, combination):
            answer.add(tuple(combination))
            if i>=len(nums): return
            helper(i+1, combination+[nums[i]])
            helper(i+1, combination)

        answer = set()
        helper(0, [])
        return [list(combination) for combination in answer]
"""
`helper()` help add `combination` to the answer.
And if we have run through all the numbers, return.
If not, for this number at index `i`, there are two scenarios.
Add it to the combination, or not.

And there might be duplicates, and I could not think of better way without using hash set on `answer`.

The time complexity is O(2^N). The space complexity is O(2^N), too.
"""


class Solution(object):
    def subsets(self, nums):
        answer = [[]]
        for n in nums:
            new_subs = []
            for sub in answer:
                new_subs.append(sub+[n])
            answer.extend(new_subs)
        return answer
"""
So for each n in `nums`, what we do is
```
new_subs = []
for sub in answer:
    new_subs.append(sub+[n])
answer.extend(new_subs)
```
We take all the subset in the `answer`, append n, put the new subset into `new_subs`.
And the answer become `subsets` + `new subsets`.
You can think of it as
`subsets` => the combination which we did not take n.
`new subsets` => the combination which we take n.

Now if we have iterated the third element, then the `answer` now contains all the possible subsets, the combination which we took the third element, and the combination which we did not take the third element.

The time complexity is O(2^N). The space complexity is O(2^N), too.
(This solution is in spired by @ZitaoWang's elegant solution)
"""

#DFS
class Solution(object):
    def subsets(self, nums):
        def dfs(path, nums):
            opt.append(path)
            if len(nums)==0: return
            for i, num in enumerate(nums):
                dfs(path+[num], nums[i+1:])

        opt = []
        dfs([], nums)
        return opt
