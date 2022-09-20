"""
Time: O(M * 4 * 3^(L-1)), M is board elements count, L is the average word length.
Space: O(N), N is the number of char in the words

This solution will TLE. We need to further "prune" the trie once we reach the leaf node.
"""
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEnd = False
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r, c, node, word):
            if c<0 or r<0 or c==COLS or r==ROWS: return
            if board[r][c] not in node.children: return
            if (r, c) in visited: return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                ans.add(word)
                node.isEnd = False
                
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            
            visited.remove((r, c))
        
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
            
        ROWS = len(board)
        COLS = len(board[0])
        
        visited = set()
        ans = set()
        node = root
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, '')
        return ans