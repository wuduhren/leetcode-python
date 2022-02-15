class Solution(object):
    def shortestDistance(self, maze, start, destination):
        N, M = len(maze), len(maze[0])
        i0, j0 = start
        pq = [(0, i0, j0, 'stop')]
        visited = set()
        
        
        while pq:
            dis, i, j, direction = heapq.heappop(pq)
            if (i, j, direction) in visited: continue
            visited.add((i, j, direction))
            
            if i<0 or i>=N or j<0 or j>=M: continue
            if maze[i][j]==1: continue
            
            if i==destination[0] and j==destination[1] and direction=='stop': return dis
                
            if direction=='stop':
                heapq.heappush(pq, (dis+1, i-1, j, 'left'))
                heapq.heappush(pq, (dis+1, i+1, j, 'right'))
                heapq.heappush(pq, (dis+1, i, j-1, 'down'))
                heapq.heappush(pq, (dis+1, i, j+1, 'up'))
            elif direction=='left':
                if i-1<0 or i-1>=N or j<0 or j>=M or maze[i-1][j]==1:
                    heapq.heappush(pq, (dis, i, j, 'stop'))
                else:
                    heapq.heappush(pq, (dis+1, i-1, j, direction))
            elif direction=='right':
                if i+1<0 or i+1>=N or j<0 or j>=M or maze[i+1][j]==1:
                    heapq.heappush(pq, (dis, i, j, 'stop'))
                else:
                    heapq.heappush(pq, (dis+1, i+1, j, direction))
            elif direction=='down':
                if i<0 or i>=N or j-1<0 or j-1>=M or maze[i][j-1]==1:
                    heapq.heappush(pq, (dis, i, j, 'stop'))
                else:
                    heapq.heappush(pq, (dis+1, i, j-1, direction))
            elif direction=='up':
                if i<0 or i>=N or j+1<0 or j+1>=M or maze[i][j+1]==1:
                    heapq.heappush(pq, (dis, i, j, 'stop'))
                else:
                    heapq.heappush(pq, (dis+1, i, j+1, direction))
                    
        return -1