"""
Time: O(N^2 * LogN^2) = O(N^2 * 2LogN) = O(N^2LogN), N is the number of elements in a row or column.
Space: O(N^2)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        h = [(grid[0][0], 0, 0)]
        
        while h:
            t, r0, c0 = heapq.heappop(h)
            
            if (r0, c0) in visited: continue
            visited.add((r0, c0))
            if r0==ROWS-1 and c0==COLS-1: return t
            
            for r, c in ((r0+1, c0), (r0-1, c0), (r0, c0+1), (r0, c0-1)):
                if r<0 or c<0 or r>=ROWS or c>=COLS: continue
                if (r, c) in visited: continue
                heapq.heappush(h, (max(t, grid[r][c]), r, c))