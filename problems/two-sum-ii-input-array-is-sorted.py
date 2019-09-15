"""
We put `l` and `r` at the beginning and at the end of the array.
Everytime with new pair of `l` and `r`, we check if its sum is target. If true, return the answer.
If the sum is larger than the target, we need to reduce the sum, and the only way to do that is to move `r` leftward, since `l` is already at the leftmost.
If the sum is smaller than the target, we need to increase the sum, and the only way to do that is to move `l` rightward, since `r` is already at the rightmost.

The time complexity is O(N).
The space complexity is O(1).
"""
class Solution(object):
    def twoSum(self, numbers, target):
        r, l = len(numbers)-1, 0
        while r>l:
            if numbers[r]+numbers[l]==target:
                return [l+1, r+1]
            elif numbers[r]+numbers[l]>target:
                r = r-1
            else:
                l = l+1
        return []

"""
We use a hashmap to keep track of all the number we went through.
Since we exactly know what we are looking for (`target-n`), we can check if the counter part is in the hashmap or not.
If true, return the answer.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        memo = {}
        for i, n in enumerate(numbers):
            if target-n in memo:
                return [memo[target-n]+1, i+1]
            memo[n] = i
