"""
Time: O(NLogN) for sorting the products, N is the number of product. O(SLogN) for search, S is the number of char of the searchWord.
Space: O(1)

Sort the products then binary search it.
"""
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        def search(products, word):
            l = 0
            r = len(products)-1
            n = len(word)
            
            while l<=r:
                m = (l+r)/2
                if products[l].startswith(word): return getTop3(products, word, l)
                if products[r].startswith(word): return getTop3(products, word, r)
                if products[m].startswith(word): return getTop3(products, word, m)
                
                if products[m][:n]>word:
                    r = m-1
                else:
                    l = m+1
                
            return []
        
        def getTop3(products, word, i):
            suggestion = []
            
            while i-1>=0 and  products[i-1].startswith(word):
                i -= 1
            
            for j in xrange(i, min(len(products), i+3)):
                if not products[j].startswith(word): break
                suggestion.append(products[j])
            return suggestion
        
        
        ans = []
        products.sort()
        
        currSearchWord = ''
        for c in searchWord:
            currSearchWord += c
            ans.append(search(products, currSearchWord))
            
        return ans


        
"""
Time: O(M) + O(S^2) ~= O(M). M is the number of char in products. S is number of char of a searchWord.
O(M) to build trie. O(len(prefix)) (~= O(S/2)) to get to the prefix node, and it will perform S time. O(1) to get top 3.
Space: O(M)

Use Trie to store the relation and search it.
"""
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

