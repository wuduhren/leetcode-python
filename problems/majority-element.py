"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def majorityElement(self, nums):
        counter = {}
        
        for n in nums:
            if n not in counter: counter[n] = 0
            counter[n] += 1
            if counter[n]>len(nums)/2.0: return n
        
        return 0

"""
Time: O(N)
Space: O(1)

Boyer-Moore
If a number `n` is not majority number its `count` will certainly become 0 and `ans` will switch to another number `n`.
If a number `n` is majority number its `count` will certainly larger thans 0 at the end, since it is the "majority".
"""
class Solution(object):
    def majorityElement(self, nums):
        ans = nums[0]
        count = 0
        
        for n in nums:
            if n==ans:
                count += 1
            else:
                count -= 1
                if count==0:
                    ans = n
                    count = 1
        return ans
                