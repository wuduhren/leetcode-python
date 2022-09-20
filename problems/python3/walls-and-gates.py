class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def bfs(i0, j0) -> None:
            q = collections.deque([(i0+1, j0, 1), (i0-1, j0, 1), (i0, j0+1, 1), (i0, j0-1, 1)])
            visited = set()
            
            while q:
                i, j, dis = q.popleft()
                
                if i<0 or j<0 or i>=MAX_ROW or j>=MAX_COL: continue
                if rooms[i][j]==0 or rooms[i][j]==-1: continue
                if (i, j, dis) in visited: continue
                visited.add((i, j, dis))
                
                if dis<rooms[i][j]:
                    rooms[i][j] = dis
                    q.append((i+1, j, dis+1))
                    q.append((i-1, j, dis+1))
                    q.append((i, j+1, dis+1))
                    q.append((i, j-1, dis+1))
                
        MAX_ROW = len(rooms)
        MAX_COL = len(rooms[0])
        
        for i in range(MAX_ROW):
            for j in range(MAX_COL):
                if rooms[i][j]==0:
                    bfs(i, j)
        return rooms