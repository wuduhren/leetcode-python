"""
If we use the solution from the [last question](https://leetcode.com/problems/subsets/),
We will notice that it will have some duplicates.
This is because if you have three 2 (`[2, 2, 2]`).
You might choosing two different sets of 2 and end up looking the same.
For example, you choose the first and the second => `[2, 2]`
You choose the second and the third => `[2, 2]`

One workaround I did is just using hash-set.
```
return list(set([tuple(combination) for combination in answer]))
```
This cause us really high time complexity.
Since turning list to tuple and tuple to list is actually O(N) in theory.

Time complexity would be `O((2^N) * N)` be cuase for each element in the answer we need to convert it to tuple and back.
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        answer = [[]]
        for num in nums:
            new_subs = []
            for sub in answer:
                new_subs.append(sub+[num])
            answer.extend(new_subs)
        return list(set([tuple(combination) for combination in answer]))

"""
I found the best solution and explaination is made by @ZitaoWang's answer and here is his [explaination](https://leetcode.com/problems/subsets-ii/discuss/171626/Python-solution). I copied from it.
For example, `nums = [1,1,2,2,2,4,4,5]`. In this case, `counter = {1:2, 2:3, 4:2, 5:1}`.
We intialize `answer = [[]]` and build the solution iteratively as we loop over the counter.
We first reach `num, count = 1, 2`. The power set of [1,1] is `[[], [1], [1,1]]`.
Then we reach `num, count = 2, 3`.
The power set of [1,1,2,2,2] is obtained by appending either zero, one, two or three 2's to all elements in `answer`.
After which we get answer = [[], [1], [1,1], [2], [1,2], [1,1,2],[2,2], [1,2,2], [1,1,2,2],[2,2,2], [1,2,2,2], [1,1,2,2,2]].
After we loop over counter, answer will be the power set of nums.

Time complexity: `O(2^N)`, space complexity: `O(2^N)`.
"""
from collections import Counter

class Solution(object):
    def subsetsWithDup(self, nums):
        counter = Counter(nums)
        answer = [[]]

        for num, count in counter.items():
            power_set = [[num]*c for c in xrange(1, count+1)]
            for i in xrange(len(answer)):
                for s in power_set:
                    answer.append(answer[i]+s)
        return answer


#DFS
class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()

        def dfs(path, nums):
            opt.append(path)
            if len(nums)==0: return
            for i, num in enumerate(nums):
                if i>0 and nums[i]==nums[i-1]: continue
                dfs(path+[num], nums[i+1:])
        opt = []
        dfs([], nums)
        return opt


