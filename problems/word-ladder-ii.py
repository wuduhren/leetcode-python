class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        #build an adjacent list
        a = collections.defaultdict(list)
        
        for word in wordList+[beginWord]:
            for i in xrange(len(word)):
                s = word[:i]+'#'+word[i+1:]
                a[s].append(word)
        
        #BFS
        q = collections.deque([(beginWord, collections.OrderedDict())])
        ans = []
        shortest = float('inf')
        
        while q:
            word, path = q.popleft()

            if word in path: continue
            path[word] = None
            if len(path)>shortest: break
            
            if word==endWord:
                shortest = len(path)
                ans.append(path.keys())
                continue

            for i in xrange(len(word)):
                s = word[:i]+'#'+word[i+1:]
                for wordNext in a[s]:
                    q.append((wordNext, path.copy()))
            
        return ans
    
"""
Time: O(VL+E).
Building V ajacencyList takes O(V*L*26) => O(VL). DFS takes O(V+E)
V is the number of words. L is the length of each word. E is the number of edge of each vertext (word).
Space: O(V+E)

Build a special ranked adjacency list.
Different from the normal adjacency list, the list will only contain the ones the is farther away from the beginWord.
In other words, the adjacency nodes you get will not will not cercle back to the direction of the beginWord.
This assures us the result will be "shortest" path.

Next, only standard dfs is needed.

If you did not build the special adjacency list, you might need to check if a new node is already in the path or not.
This will cause TLE.
Or cause MLE if you use a hashset for the visited node in the path...

This solution is inspired by https://www.youtube.com/watch?v=mIZJIuMpI2M.
"""
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        ans = []
        wordSet = set(wordList)
        ajacencyList = self.buildAjacencyList(beginWord, wordSet)
        stack = [(beginWord, [beginWord])]
        
        while stack:
            word, path = stack.pop()
            if word==endWord: ans.append(path)
            
            for nextWord in ajacencyList[word]:
                stack.append((nextWord, path+[nextWord]))

        return ans
    
    def buildAjacencyList(self, beginWord, wordSet):
        ajacencyList = collections.defaultdict(list)
        
        rank = {}
        rank[beginWord] = 0
        
        q = collections.deque()
        q.append(beginWord)
        
        while q:
            word = q.popleft()
            for i in xrange(len(word)):
                for alphabet in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i]+alphabet+word[i+1:]
            
                    if nextWord not in wordSet or word==nextWord: continue

                    if nextWord not in rank:
                        rank[nextWord] = rank[word]+1
                        ajacencyList[word].append(nextWord)
                        q.append(nextWord)
                    elif rank[word]<rank[nextWord]:
                        ajacencyList[word].append(nextWord)
        
        return ajacencyList