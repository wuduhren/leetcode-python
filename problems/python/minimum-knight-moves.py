# Bidirectional BFS
class Solution(object):
    def minKnightMoves(self, x, y):
        offsets = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        q1 = collections.deque([(0, 0)])
        q2 = collections.deque([(x, y)])
        steps1 = {(0, 0): 0} #steps needed starting from (0, 0)
        steps2 = {(x, y): 0} #steps needed starting from (x,y)
        
        while q1 and q2:
            i1, j1 = q1.popleft()
            if (i1, j1) in steps2: return steps1[(i1, j1)]+steps2[(i1, j1)]
            
            i2, j2 = q2.popleft()
            if (i2, j2) in steps1: return steps1[(i2, j2)]+steps2[(i2, j2)]
            
            for ox, oy in offsets:
                nextI1 = i1+ox
                nextJ1 = j1+oy
                if (nextI1, nextJ1) not in steps1:
                    q1.append((nextI1, nextJ1))
                    steps1[(nextI1, nextJ1)] = steps1[(i1, j1)]+1
                
                nextI2 = i2+ox
                nextJ2 = j2+oy
                if (nextI2, nextJ2) not in steps2:
                    q2.append((nextI2, nextJ2))
                    steps2[(nextI2, nextJ2)] = steps2[(i2, j2)]+1
                
        return float('inf')