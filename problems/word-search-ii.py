# TLE
class Solution(object):
    def findWords(self, board, words):
        def getNeighbor(i, j):
            opt = []
            if i+1<M: opt.append((i+1, j))
            if j+1<N: opt.append((i, j+1))
            if i-1>=0: opt.append((i-1, j))
            if j-1>=0: opt.append((i, j-1))
            return opt

        def dfs(i, j, l, word):
            if word in found: return
            if board[i][j]!=word[l]: return

            if l==len(word)-1 and board[i][j]==word[l]:
                opt.append(word)
                found.add(word)
                return

            char = board[i][j]
            board[i][j] = '#'

            for ni, nj in getNeighbor(i, j):
                dfs(ni, nj, l+1, word)

            board[i][j] = char

        opt = []
        M = len(board)
        N = len(board[0])
        found = set()

        for i in xrange(M):
            for j in xrange(N):
                for word in words:
                    if word not in found:
                        dfs(i, j, 0, word)
        return opt


board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

print Solution().findWords(board, words)




class Solution(object):
    def findWords(self, board, words):
        def dfs(i, j, parent):
            c = board[i][j]
            node = parent[c]
            
            if '.' in node: ans.append(node.pop('.'))
            
            board[i][j] = '#'
            
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = i + rowOffset, j + colOffset     
                if newRow<0 or newRow>=len(board) or newCol<0 or newCol>=len(board[0]): continue
                if not board[newRow][newCol] in node: continue
                dfs(newRow, newCol, node)
            
            board[i][j] = c
            if not node: parent.pop(c)
                
        trie = {}
        ans = []
        
        #build trie
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['.'] = word
        print trie
        
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] in trie: dfs(i, j, trie)
        
        
        return ans
                    
            
                
        