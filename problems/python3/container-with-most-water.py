"""
Time: O(N)
Space: O(1)

i and j starts from the leftest and rightest. Move the one that has less height.

Why we won't miss any i and j?
For example, currently i is heigher than j.
If between i~j, there are no height that is larger or equal to i, than since the area is `min(height[i], height[j]) * (j-i)`, you cannot find any area that is larger than the current one.
If between i~j, there is a height that is larger or equal to i, j will on it, and it will be tested.
Thus, given any i and j, any other future i and j that have the potential of forming larger area will be tested.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        ans = 0
        
        while i<j:
            ans = max(ans, min(height[i], height[j]) * (j-i))
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return ans



class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        ans = 0
        
        while i<j:
            ans = max(ans, min(height[i], height[j]) * abs(i-j))
            
            if height[i]>height[j]:
                j -= 1
            else:
                i += 1
        return ans