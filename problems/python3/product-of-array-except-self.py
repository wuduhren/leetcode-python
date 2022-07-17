class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #left[i] := product of all nums left of nums[i] (not include nums[i])
        left = [1]
        temp = 1
        for num in nums:
            temp *= num
            left.append(temp)
        
        #right[i] := product of all nums right of nums[i] (not include nums[i])
        right = []
        temp = 1
        for num in reversed(nums):
            temp *= num
            right.append(temp)
        right.reverse()
        right.append(1)
        right = right[1:]
        
        ans = []
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        return ans

#In Place
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0]*N
        
        #generate "left"
        ans[0] = 1
        for i in range(1, N):
            ans[i] = ans[i-1]*nums[i-1]
        
        #generate "right"
        temp = 1
        for i in range(N-2, -1, -1):
            temp *= nums[i+1]
            ans[i] *= temp
        
        return ans
            
    
    