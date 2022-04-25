"""
Iterate through the board.
When we spot a starting point, we `dfs()` to see if it can finish the word.
To prevent travel to the visited node, we use a hash-set `set()` to keep track of what we have visited.
`l` is the index of the character in the `word` we are checking.
Note that we need to use `visited.copy()` to copy a whole new hash-set, or all the `dfs()` will use the same hash-set, which is not what we want.

The time complexity is `O(N^2)`, `N` is the number of nodes. You can think of it as for each node, we have to decided to go ot not to go, and we need to make the decision `MN` times.
The space complexity is `O(W*N)`, `W` is the length of `word`. Because the recursion level is `W`, and for each recursion we need to keep track of `visited`, which potensially takes `O(N)`.
"""
class Solution(object):
    def exist(self, board, word):
        def getNeighbor(i, j):
            opt = []
            if i+1<M: opt.append((i+1, j))
            if j+1<N: opt.append((i, j+1))
            if i-1>=0: opt.append((i-1, j))
            if j-1>=0: opt.append((i, j-1))
            return opt

        def dfs(i, j, l, visited):
            if l==len(word)-1: return True
            visited.add((i, j))
            for ni, nj in getNeighbor(i, j):
                if (ni, nj) not in visited and board[ni][nj]==word[l+1]:
                    if dfs(ni, nj, l+1, visited.copy()): return True
            return False

        M = len(board)
        N = len(board[0])

        for i in xrange(M):
            for j in xrange(N):
                if board[i][j]==word[0]:
                    if dfs(i, j, 0, set()): return True

        return False

"""
As you see, the above solution takes lots of space.
Another way is to change the character on the `board` to `#` to represent it as visited.
After the `dfs()` call we need to change it back. Because other branch of `dfs()` might not need visit this node, or haven't visit this node.

The time complexity is `O(N^2)`, `N` is the number of nodes.
The space complexity is `O(W)`, `W` is the length of `word`. Because the recursion level is `W`.
This answer is inspired by @caikehe's [solution](https://leetcode.com/problems/word-search/discuss/27660/).
"""
class Solution(object):
    def exist(self, board, word):
        def getNeighbor(i, j):
            opt = []
            if i+1<M: opt.append((i+1, j))
            if j+1<N: opt.append((i, j+1))
            if i-1>=0: opt.append((i-1, j))
            if j-1>=0: opt.append((i, j-1))
            return opt

        def dfs(i, j, l):
            if l==len(word)-1 and board[i][j]==word[l]: return True
            if board[i][j]!=word[l]: return False

            char = board[i][j]
            board[i][j] = '#'

            for ni, nj in getNeighbor(i, j):
                if dfs(ni, nj, l+1): return True

            board[i][j] = char
            return False

        M = len(board)
        N = len(board[0])

        for i in xrange(M):
            for j in xrange(N):
                if dfs(i, j, 0): return True

        return False
