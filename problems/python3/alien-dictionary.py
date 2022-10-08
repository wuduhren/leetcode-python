class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = collections.defaultdict(list)
        inbounds = collections.Counter()
        q = collections.deque()
        ans = ''
        
        adj = {c: set() for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen]==w2[:minLen] and len(w1)>len(w2): return ""
            
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        for c in adj:
            for nc in list(adj[c]):
                inbounds[nc] += 1
        
        for c in adj:
            if inbounds[c]==0: q.append(c)
        
        while q:
            c = q.popleft()
            
            ans += c
            
            for nc in adj[c]:
                inbounds[nc] -= 1
                if inbounds[nc]==0: q.append(nc)
        
        return ans if len(ans)==len(adj) else ''

