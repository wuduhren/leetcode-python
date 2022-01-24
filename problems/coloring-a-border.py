"""
A node is on the "border" if 
1. It is on the actual border of the grid.
Or
2. Any of its neighbor has different color.

BFS the grid starting from (row, col), if the node "isBorder" add it to nodesToColor.
Color the nodes in the nodesToColor.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def colorBorder(self, grid, row, col, color):
        def isValid(i, j):
            return i>=0 and j>=0 and i<len(grid) and j<len(grid[0])
        
        def isBorder(i, j, color):
            if i==0 or i==len(grid)-1 or j==0 or j==len(grid[0])-1: return True
            if any(grid[iNei][jNei]!=color for iNei, jNei in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]): return True
            return False
            
        q = collections.deque([(row, col)])
        nodesToColor = []
        visited = set()
        
        while q:
            i, j = q.popleft()
            
            if not isValid(i, j): continue
            if grid[i][j]!=grid[row][col]: continue
            if (i, j) in visited: continue
            visited.add((i, j))
            
            if isBorder(i, j, grid[row][col]): nodesToColor.append((i, j))
            
            for iNext, jNext in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                q.append((iNext, jNext))
        
        for i, j in nodesToColor:
            grid[i][j] = color
        
        return grid