"""
[0] For each height, if the it is lower than the previous one, it means that the previous are not able to extend anymore. So we calculate its area.

[1] If the previous area, is larger than the current one, it means that the current one are able to extand backward.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        heights.append(0) #dummy for the ending
        
        for i, h in enumerate(heights):
            start = i
            while stack and h<stack[-1][1]: #[0]
                j, h2 = stack.pop()
                maxArea = max(maxArea, h2*(i-j))
                start = j
            stack.append((start, h)) #[1]
        
        return maxArea