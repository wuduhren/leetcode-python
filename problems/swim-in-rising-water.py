"""
Starting from `(0, 0)` we keep on selecting the neighbor with lower elevation until we reach the end.
There are four possible neighbors `(i+1, j), (i-1, j), (i, j+1), (i, j-1)`.
Every time we select neighbor  we check if we visited and choose the smallest elevation to go.
"""
#Wrong
class Solution(object):
    def swimInWater(self, grid):
        def getNext(i, j):
            options = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
            elevation = float('inf')
            opt = (None, None)
            for i_next, j_next in options:
                if i_next<0 or i_next>=N or j_next<0 or j_next>=M: continue
                if (i_next, j_next) in visited: continue
                if grid[i_next][j_next]<elevation:
                    elevation = grid[i_next][j_next]
                    opt = (i_next, j_next)
            return opt

        N = len(grid)
        M = len(grid[0])
        ans = grid[-1][-1]
        visited = set()
        i = j = 0

        while i<N-1 and j<M-1:
            print i, j
            visited.add((i, j))
            ans = max(ans, grid[i][j])
            i, j = getNext(i, j)
        return ans

"""
The above solution is worng, because we might reach a point which all its neighbor is visited (dead end).
That is why we need a heap to get the next posible point to go.
And when we reach dead end, we pop out the next avaliable option.
The time complexity is O((N^2)*LogN), for there are N^2 point and every heap operation for it is LogN.
Space complexity is O(N^2)
"""
#Heap solution
class Solution(object):
    def swimInWater(self, grid):
        ans = grid[-1][-1]
        N = len(grid)
        pq = []
        seen = set()

        heapq.heappush(pq, (grid[0][0], 0, 0))
        while pq:
            t, i, j = heapq.heappop(pq)
            ans = max(ans, t)
            if i==N-1 and j==N-1: return ans
            for i_next, j_next in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if i_next<0 or i_next>=N or j_next<0 or j_next>=N: continue
                if (i_next, j_next) in seen: continue
                heapq.heappush(pq, (grid[i_next][j_next], i_next, j_next))
                seen.add((i_next, j_next))
        return ans


"""
The answer must lie between `l` and `h`.
Where h is the value we sure that it can pass, l is the value it might or might not pass.
So we gradually test the value between `l~h` by binary search.
Until we find the value which is the lowest possible time that can pass. #[0]

I init the `l` with the `t` of the destination, because we couldn't have been reach the destination without using `t` amount of time.
I init the `h` with the max `t` in the entire grid, since we can swim withim this time no matter what.

The function `canPassWtihTimeLimit(t)` takes a parameter `t` and use DFS to see if we can swim to the destination in the time limit t.

The time complexity is O((N^2)*LogN).
Find the max in the grid took O(N^2).
`canPassWtihTimeLimit(t)` took O(N^2), because we might possibly travel the entire grid.
We call `canPassWtihTimeLimit(t)` about O(LogN) of time because we use the binary search concept to navigate the `l` and `r`.
"""
class Solution(object):
    def swimInWater(self, grid):
        def canPassWtihTimeLimit(t):
            stack = []
            seen = set()

            if grid[0][0]<=t: stack.append((0, 0))
            while stack:
                i, j = stack.pop()
                if i==N-1 and j==N-1: return True
                seen.add((i, j))
                for i_next, j_next in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if i_next<0 or i_next>=N or j_next<0 or j_next>=N: continue
                    if (i_next, j_next) in seen: continue
                    if grid[i_next][j_next]>t: continue
                    stack.append((i_next, j_next))
            return False

        N = len(grid)
        l = grid[-1][-1]
        h = max(map(max, grid)) #get max value in the grid
        while True:
            m = (l+h)/2
            p = canPassWtihTimeLimit(m)
            if p and not canPassWtihTimeLimit(m-1): return m #[0]
            if p:
                h = m
            else:
                l = m+1
        return h





