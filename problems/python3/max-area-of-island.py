class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j) -> int:
            if i<0 or j<0 or i>=MAX_ROW or j>=MAX_COL: return 0
            if grid[i][j]==0 or grid[i][j]==2: return 0
            
            grid[i][j] = 2 #mark as visited
            
            area = 1
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area
            
        ans = 0
        MAX_ROW = len(grid)
        MAX_COL = len(grid[0])
        
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                ans = max(ans, dfs(i, j))
        return ans