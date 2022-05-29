#https://leetcode.com/problems/two-sum/
"""
when we iterate through the nums
we don't know if the counter part exist
so we store the counter part we want in the 'wanted' with the index now
so inside the wanted is {the_counter_part_we_want:index_now} [0]

later on if we found the num is in 'wanted'
we return the index_now and the index_now we previously stored in the 'wanted' [1]
"""
class Solution(object):
    def twoSum(self, nums, target):
        wanted = {}
        for i in xrange(len(nums)):
            n = nums[i]
            if n in wanted: #[1]
                return [wanted[n], i]
            else:
                wanted[target-n] = i #[0]
        return []



#2021/5/17
class Solution(object):
    def twoSum(self, nums, target):
        M = {} #counter part number needed by index i: i
        
        for i, num in enumerate(nums):
            if num in M: return (M[num], i)
            M[target-num] = i
        
        return False

#2021/7/4
class Solution(object):
    def twoSum(self, nums, target):
        memo = {} #{key : value} := {"counter part needed for n" : "index of n"}
        
        for i, n in enumerate(nums):
            if n in memo:
                return [memo[n], i]
            else:
                memo[target-n] = i
        return []

#2021/7/31
"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def twoSum(self, nums, target):
        memo = {} #{key : value} := {"counter part needed for n" : "index of n"}
        
        for i, n in enumerate(nums):
            if n in memo: return [memo[n], i]
            memo[target-n] = i
        
        return []