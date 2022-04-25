class NumArray(object):
    def __init__(self, nums):
        #total[i] = nums[0]+nums[1]+...+nums[i]
        self.total = []
        
        #initialize total
        temp = 0
        for num in nums:
            temp += num
            self.total.append(temp)
        
    def sumRange(self, i, j):
        return self.total[j] - self.total[i-1] if i>0 else self.total[j]