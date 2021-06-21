"""
Let's calculate the answer considering only the left boandary.
The water each i can contain is wall[i-1]-height[i]
if no water at i-1 the wall[i-1] will be height[i-1], else it should be height[i-1]+water[i-1]
=> water[i] = (height[i-1] + water[i-1]) - height[i] (l2r below)

Do the same from right to left, this time considering only the right boandary.

The amount of water at i considering both left and right wall will be min(l2r[i], r2l[i])
"""
class Solution(object):
    def trap(self, height):
        N = len(height)
        l2r = [0]*N #water
        r2l = [0]*N #water
        
        for i in xrange(1, N):
            l2r[i] = max(l2r[i-1]+height[i-1]-height[i], 0)
        
        for i in xrange(N-2, -1, -1):
            r2l[i] = max(r2l[i+1]+height[i+1]-height[i], 0)
        
        ans = 0
        for i in xrange(N):
            ans += min(l2r[i], r2l[i])
        return ans