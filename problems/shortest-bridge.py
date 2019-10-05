"""
First, identify one of the island by marking its value by 2 (island2). [0]

Second ([1]), use BFS to go through another island (island1). When we encounter 0 we put it on `q2`, otherwise `q`.
When q is finished, it means that the island1 is completely explored (all `(i, j)` is in the `visied`).
Now we make put `q2` to the `q` and clear `q2`. [2]

When q is finished, it means that all of the one-tile outward `(i, j)` is explored (in the `visited`).
Now we make put `q2` to the `q` and clear `q2`.

When q is finished, it means that all of the two-tile outward `(i, j)` is explored (in the `visited`).
Now we make put `q2` to the `q` and clear `q2`.

...

We keep on doing this until we find the island2. [3]

The time complexity is `O(N)`, `N` is the number of element in `A`.
The space complexity is `O(N)`, too. Since we might put most of the `(i, j)` in the `visited`.

Of course, we can optimize the space, by changing the value in the `A`.
The code would be a little bit harder the read and understand.
I challenge you to try it out!
"""
class Solution(object):
    def shortestBridge(self, A):
        def findFirst(target):
            for i in xrange(M):
                for j in xrange(N):
                    if A[i][j]==target: return (i, j)

        M, N = len(A), len(A[0])

        #[0]
        q = collections.deque([findFirst(1)])
        while q:
            i, j = q.popleft()
            if i<0 or i>=M: continue
            if j<0 or j>=N: continue
            if A[i][j]==2 or A[i][j]==0: continue
            if A[i][j]==1: A[i][j] = 2
            q.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        #[1]
        q.append(findFirst(1))
        q2 = []
        tile = 0
        visited = set()
        while q or q2:
            if not q: #[2]
                q.extend(q2)
                q2 = []
                tile+=1

            i, j = q.popleft()
            if (i, j) in visited: continue
            visited.add((i, j))

            if A[i][j]==2: return tile #[3]

            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if ni<0 or ni>=M: continue
                if nj<0 or nj>=N: continue
                if A[ni][nj]==0:
                    q2.append((ni, nj))
                else:
                    q.append((ni, nj))

        return tile #should not comes here

