class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        
        timeInfo = []
        for i in range(N):
            timeInfo.append((position[i], (target-position[i])/speed[i]))
        timeInfo.sort(reverse=True)
        
        stack = []
        for _, time in timeInfo:
            stack.append(time)
            if len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        
        return len(stack)