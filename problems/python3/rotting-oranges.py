class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rotten = set()
        aboutToRot = set()
        fresh = set()
        
        for i in range(len(grid)):
            for j in range((len(grid[0]))):
                if grid[i][j]==2:
                    rotten.add((i, j))
                elif grid[i][j]==1:
                    fresh.add((i, j))
        
        while rotten:
            i0, j0 = rotten.pop() #randomly get one
            grid[i0][j0] = 2
            
            for i, j in ((i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1)):
                if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]): continue
                if (i, j) in rotten or (i, j) in aboutToRot: continue
                if (i, j) in fresh:
                    fresh.remove((i, j))
                    aboutToRot.add((i, j))
            
            if not rotten and not aboutToRot: break
            
            if not rotten:
                time += 1
                rotten = aboutToRot
                aboutToRot = set()
                
        if fresh: return -1
        
        return time