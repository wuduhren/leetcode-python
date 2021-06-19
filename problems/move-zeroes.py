#https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        # Loop through the array
        # Find the first number that are not 0
        # Switch it with the nums[0]
        # Now nums[0] has the right value
        #
        # Find the second number that are not 0
        # Switch it with the nums[1]
        # Now nums[1] has the right value
        # ...
        
        cursor = 0 #the array index sorted so far
        for i in range(0, len(nums)):
            num = nums[i]
            if num!=0:
                temp = nums[cursor]
                nums[cursor] = nums[i]
                nums[i] = temp
                cursor+=1


"""
j is the index to insert when a number not equal to 0.
After all the non-zero numbers are inplace, the rests are all zeros.
"""
class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        
        for n in nums:
            if n!=0:
                nums[j] = n
                j += 1
        
        for i in xrange(j, len(nums)):
            nums[i] = 0
        
        return nums