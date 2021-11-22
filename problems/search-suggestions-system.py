class Node(object):
    def __init__(self, c):
        self.c = c
        self.nexts = {}

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        ans = []
        root = Node('')
        
        #build trie
        for product in products:
            curr = root
            for c in product+'.':
                if c not in curr.nexts:
                    curr.nexts[c] = Node(c)
                curr = curr.nexts[c]
        
        # search top3 for each prefix
        curr = root
        for i, c in enumerate(searchWord):
            if c not in curr.nexts: break
            curr = curr.nexts[c]
            ans.append(self.getTop3(searchWord[:i+1], curr))
                
        ans += [[] for _ in xrange(len(searchWord)-len(ans))]
        return ans
    
    def getTop3(self, prefix, node):
        def helper(prefix, node):
            if len(top3)>=3: return
            if '.' in node.nexts: top3.append(prefix)
                
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c in node.nexts:
                    helper(prefix+c, node.nexts[c])
        
        top3 = []
        helper(prefix, node)
        return top3