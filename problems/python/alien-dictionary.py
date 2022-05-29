"""
Topological Sort
"""
class Solution(object):
    def alienOrder(self, words):
        #return true if cycles are detected.
        def dfs(c):
            if c in path: return True
            if c in visited: return False
            path.add(c)
            for nei in adj[c]:
                if dfs(nei): return True
            res.append(c)
            path.remove(c)
            visited.add(c)
            return False
        
        #build adjacency list
        adj = {c: set() for word in words for c in word}
        for i in xrange(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen]==w2[:minLen] and len(w1)>len(w2): return ""
            
            for j in xrange(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        #topological sort
        path = set() #path currently being reversed
        visited = set() #done processing
        res = []
        for c in adj:
            if dfs(c): return ""
            
        return "".join(reversed(res))