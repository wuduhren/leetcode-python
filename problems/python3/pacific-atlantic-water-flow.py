class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(q, ocian):
            while q:
                i0, j0 = q.popleft()
                if (i0, j0) in ocian: continue
                ocian.add((i0, j0))
                
                for i, j in ((i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1)):
                    if i<0 or j<0 or i>=MAX_ROW or j>=MAX_COL: continue
                    if heights[i][j]>=heights[i0][j0]: q.append((i, j))
                    
        MAX_ROW = len(heights)
        MAX_COL = len(heights[0])
        
        #add the top and left to q1
        pacific = set()
        q1 = collections.deque()
        for j in range(MAX_COL): q1.append((0, j))
        for i in range(MAX_ROW): q1.append((i, 0))
            
        #add botton and right to q2
        atlantic = set()
        q2 = collections.deque()
        for j in range(MAX_COL): q2.append((MAX_ROW-1, j))
        for i in range(MAX_ROW): q2.append((i, MAX_COL-1))
            
        bfs(q1, pacific)
        bfs(q2, atlantic)
        return pacific.intersection(atlantic)