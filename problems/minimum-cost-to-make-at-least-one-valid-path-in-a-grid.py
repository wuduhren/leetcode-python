class Solution(object):
    def minCost(self, grid):
        pq = [(0, False, 0, 0, 0)]
        visited = set()
        M = len(grid)
        N = len(grid[0])
        
        while pq:
            cost, modified, direction, x, y = heapq.heappop(pq)
            if x<0 or x>=M or y<0 or y>=N: continue
            if (direction, x, y) in visited: continue
            visited.add((direction, x, y))
            
            if x==M-1 and y==N-1: return cost
            
            if direction==0: direction = grid[x][y]

            if direction==1:
                heapq.heappush(pq, (cost, False, 0, x, y+1))
            elif direction==2:
                heapq.heappush(pq, (cost, False, 0, x, y-1))
            elif direction==3:
                heapq.heappush(pq, (cost, False, 0, x+1, y))
            elif direction==4:
                heapq.heappush(pq, (cost, False, 0, x-1, y))
        
            if not modified:    
                for d in [1,2,3,4]:
                    if d==grid[x][y]: continue
                    heapq.heappush(pq, (cost+1, True, d, x, y))
                            
        return float('inf')