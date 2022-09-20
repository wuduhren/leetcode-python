class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i<0 or j<0 or i>=MAX_ROWS or j>=MAX_COLS: return
            if grid[i][j]!='1': return
            
            grid[i][j] = '2'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        count = 0
        MAX_ROWS = len(grid)
        MAX_COLS = len(grid[0])
        
        for i in range(MAX_ROWS):
            for j in range(MAX_COLS):
                if grid[i][j]=='1':
                    dfs(i, j)
                    count += 1
        return count