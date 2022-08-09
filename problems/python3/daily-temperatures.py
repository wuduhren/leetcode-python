class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                prevTemp, prevIndex = stack.pop()
                ans[prevIndex] = i-prevIndex
            stack.append((temp, i))
        
        return ans