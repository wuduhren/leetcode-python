"""
Time: O(NxM^2). N is the number of words. M is the length of the word.
Note that, getPatterns() takes O(M^2) since creating new string will also takes O(M) and for each word we do that O(M) times.

Space: O(NxM^2)
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getPatterns(word) -> List[str]:
            patterns = []
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                patterns.append(pattern)
            return patterns
        
        
        if endWord not in wordList: return 0
        wordList.append(beginWord)
        
        #build adjacency list
        nei = collections.defaultdict(list)
        for word in wordList:
            for pattern in getPatterns(word):
                nei[pattern].append(word)
        
        #BFS
        q = collections.deque([(beginWord, 1)])
        visited = set()
        while q:
            word, steps = q.popleft()
            
            if word in visited: continue
            visited.add(word)
            if word==endWord: return steps
            
            for pattern in getPatterns(word):
                for nextWord in nei[pattern]:
                    if nextWord in visited: continue
                    q.append((nextWord, steps+1))
        return 0