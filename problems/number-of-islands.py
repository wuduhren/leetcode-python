class Solution(object):

    """
    we assume 1 means unexplored, 2 is explored
    when we discover an unexplored place we count+=1
    and use explore_adjacent() to mark the whole island to 2, so we will not count it again
    """

    #DFS
    def numIslands(self, grid):
        if grid is None or grid==[] or grid==[[]]: return 0
        
        count = 0
        height = len(grid)
        width = len(grid[0])

        #explore_adjacent() if grid[h][w] is unexplored, mark it as explored. 1->2.
        #and continue to do the same to the adjacent
        def explore_adjacent(h, w):
            #check border
            if h<0 or h>height-1: return
            if w<0 or w>width-1: return

            #if grid[h][w]==0: it is sea, return
            #if grid[h][w]==2: we already explore this place, return
            if grid[h][w]=='1':
                grid[h][w] = '2'
                explore_adjacent(h+1, w)
                explore_adjacent(h-1, w)
                explore_adjacent(h, w+1)
                explore_adjacent(h, w-1)
            return
        
        for h in range(height):
            for w in range(width):
                #if v==0: it is sea, continue to find unexplored
                #if v==2: we already explore this place, continue to find unexplored
                if grid[h][w]=='1':
                    #if we discover an unexplored place
                    #count it
                    #and set it as root to explore the whole island
                    count+=1
                    explore_adjacent(h, w)
        return count

    #BFS
    def numIslands(self, grid):
        if grid is None or grid==[] or grid==[[]]: return 0
        
        count = 0
        height = len(grid)
        width = len(grid[0])
        
        def explore_adjacent(h_root, w_root):
            if h_root<0 or h_root>height-1: return
            if w_root<0 or w_root>width-1: return

            #start the queue from root
            queue = [(h_root, w_root)]
                
            while len(queue)>0:
                coor = queue.pop(0)
                h = coor[0]
                w = coor[1]
                
                #check border
                if h<0 or h>height-1: continue
                if w<0 or w>width-1: continue
                
                if grid[h][w]=='1':
                    grid[h][w] = '2'
                    queue.extend([(h+1, w), (h-1, w), (h, w+1), (h, w-1)])

            #this function will end if there are no new adjacent to add to queue
            #which means the whole island explored (mark as 2)
            return
                    
        for h in range(height):
            for w in range(width):
                if grid[h][w]=='1':
                    #if we discover an unexplored place
                    #count it
                    #and set it as root to explore the whole island
                    count+=1
                    explore_adjacent(h, w)
                    
        return count


class Solution(object):
    def numIslands(self, grid):
        def dfs(i0, j0):
            stack = [(i0, j0)]
            
            while stack:
                i, j = stack.pop()
                if grid[i][j]=="0" or grid[i][j]=="2": continue
                grid[i][j] = "2"
                
                if i+1<M: stack.append((i+1, j))
                if 0<=i-1: stack.append((i-1, j))
                if j+1<N: stack.append((i, j+1))
                if 0<=j-1: stack.append((i, j-1))
                
        if not grid or not grid[0]: return 0
        
        count = 0
        M = len(grid)
        N = len(grid[0])
        
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]=="0" or grid[i][j]=="2": continue
                dfs(i, j)
                count += 1
        return count

"""
0 means water.
1 means land.
2 means land we already visited.

We iterate the map using a double for-loop.
When we encounter 0 or 2, we skip.
When we encounter 1, we do a dfs() to mark all the land on the same island as 2. So we don't count it again.

Time: O(N). We iterate all the island once. If visited, we will skip.
Space: O(1).
"""