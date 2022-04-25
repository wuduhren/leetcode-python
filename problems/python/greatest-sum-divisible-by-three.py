#DP
"""
Time: O(N)
Space: O(N). Can reduce to O(1).

dp[i][0] max number n, which n%3==0, considering nums[0~i-1]
dp[i][1] max number n, which n%3==1, considering nums[0~i-1]
dp[i][2] max number n, which n%3==2, considering nums[0~i-1]
"""
class Solution(object):
    def maxSumDivThree(self, nums):
        dp = [[0]*3 for _ in xrange(len(nums)+1)]
        
        for i in xrange(len(nums)+1):
            if i==0:
                dp[i][0] = 0
                dp[i][1] = float('-inf')
                dp[i][2] = float('-inf')
                continue
            
            n = nums[i-1]
            
            if n%3==0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][0]+n)
                dp[i][1] = max(dp[i-1][1], dp[i-1][1]+n)
                dp[i][2] = max(dp[i-1][2], dp[i-1][2]+n)
            elif n%3==1:
                dp[i][0] = max(dp[i-1][0], dp[i-1][2]+n)
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]+n)
                dp[i][2] = max(dp[i-1][2], dp[i-1][1]+n)
            elif n%3==2:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+n)
                dp[i][1] = max(dp[i-1][1], dp[i-1][2]+n)
                dp[i][2] = max(dp[i-1][2], dp[i-1][0]+n)
            
        return dp[-1][0]

# Greedy
class Solution(object):
    def videoStitching(self, clips, T):
        if T==0: return 0
        if not clips: return -1
        
        clips.sort()
        print clips
        
        if clips[0][0]!=0: return -1
        if clips[0][1]>=T: return 1
        
        count = 0
        i = 0
        rightMost = 0
        
        while i<len(clips):
            right = rightMost
            while i<len(clips) and clips[i][0]<=rightMost:
                right = max(right, clips[i][1])
                i += 1
            
            if rightMost==right: return -1 #rightMost cannot be update anymore
            
            rightMost = right
            count += 1
            if rightMost >= T: return count
            
        return -1