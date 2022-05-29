"""
The water stored at i is `min(leftMax, rightMax) - height[i]`
leftMax: max height left of i
rightMax: max height right of i

To use only constant space.
We can calculete the leftMax or rightMax and update ans along the way.
And we always go with the side where leftMax or rightMax is smaller.

Time: O(N)
Space: O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1
        
        leftMax = float('-inf')
        rightMax = float('-inf')
        
        while l<=r:
            if leftMax<rightMax:
                if height[l]>=leftMax:
                    leftMax = height[l]
                else:
                    ans += leftMax-height[l]
                l += 1
            else:
                if height[r]>=rightMax:
                    rightMax = height[r]
                else:
                    ans += rightMax-height[r]
                r -= 1
        return ans