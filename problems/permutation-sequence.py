class Solution(object):
    def getPermutation(self, N, K):
        K = K-1 #make it 0-index
        nums = range(1, N+1)
        ans = ''
        
        while N>0:
            a = K/math.factorial(N-1)
            ans += str(nums[a])
            nums.pop(a)
            
            K -= math.factorial(N-1)*(a+1)
            N -= 1
        return ans