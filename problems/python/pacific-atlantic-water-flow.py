class Solution(object):
    def pacificAtlantic(self, heights):
        def bfs(q, ocian):
            while q:
                i0, j0 = q.popleft()
                if (i0, j0) in ocian: continue
                ocian.add((i0, j0))
                
                for i, j in [(i0+1, j0), (i0-1, j0), (i0, j0+1), (i0, j0-1)]:
                    if i>=len(heights) or i<0 or j>=len(heights[0]) or j<0: continue
                    if heights[i][j]>=heights[i0][j0]: q.append((i, j))
                        
        pacific = set()
        altalantic = set()
        q1 = collections.deque()
        q2 = collections.deque()
        
        #add top, left to pacific
        for j in xrange(len(heights[0])): q1.append((0, j))
        for i in xrange(len(heights)): q1.append((i, 0))
            
        #add right, bottom to atalantic
        for j in xrange(len(heights[0])): q2.append((len(heights)-1, j))
        for i in xrange(len(heights)): q2.append((i, len(heights[0])-1))
        
        bfs(q1, pacific)
        bfs(q2, altalantic)
                        
        return pacific.intersection(altalantic)
                