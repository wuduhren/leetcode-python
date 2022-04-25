class Solution(object):
    def sortColors(self, nums):
        l = 0
        r = len(nums)-1
        
        i = 0
        while i<=r:
            if nums[i]==0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i]==2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            elif nums[i]==1:
                i += 1

# counting sort
class Solution(object):
    def sortColors(self, nums):
        count0 = count1 = count2 = 0
        
        for num in nums:
            if num==0:
                count0 += 1
            elif num==1:
                count1 += 1
            elif num==2:
                count2 += 1
        
        i = 0
        while count0>0:
            nums[i] = 0
            i += 1
            count0 -= 1
            
        while count1>0:
            nums[i] = 1
            i += 1
            count1 -= 1
            
        while count2>0:
            nums[i] = 2
            i += 1
            count2 -= 1