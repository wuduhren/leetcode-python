"""
dp[0][0 or 1] is considering no num in nums.
dp[1][0 or 1] is considering the first num in nums.
dp[2][0 or 1] is considering the second num in nums.
dp[3][0 or 1] is considering the third num in nums.
...

dp[i][0] := longest length of wiggle seq that ends at nums[i-1] and diff ends in positive number.
dp[i][1] := longest length of wiggle seq that ends at nums[i-1] and diff ends in negative number.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        ans = 1
        N = len(nums)
        
        dp = [[0, 0] for _ in xrange(N+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        
        for i in xrange(2, N+1):
            if nums[i-1]-nums[i-2]>0:
                dp[i][0] = dp[i-1][1]+1
                dp[i][1] = dp[i-1][1]
            elif nums[i-1]-nums[i-2]<0:
                dp[i][1] = dp[i-1][0]+1
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][1] = dp[i-1][1]
                dp[i][0] = dp[i-1][0]
                
            ans = max(ans, dp[i][0], dp[i][1])

        return ans

"""
From the above solution, we notice that we do not need whole array to keep track.
Just need two variables.
Use `up` and `down` to replace dp[i-1][0] and dp[i-1][1]

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        N = len(nums)
        
        ans = 1
        up = 1
        down = 1
        
        for i in xrange(2, N+1):
            if nums[i-1]-nums[i-2]>0:
                up, down = down+1, down
            elif nums[i-1]-nums[i-2]<0:
                down = up+1
                
            ans = max(ans, up, down)

        return ans


