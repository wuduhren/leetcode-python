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

"""
I really take time to explain my solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""