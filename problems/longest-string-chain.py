import collections

"""
DP

Time: O(NLogN)+O(NSS),

Where N is the number of words and S is the length of each word. (S<=16)
NLogN is for sorting words. NSS is for the double for-loop.

Space: O(NS)
"""
class Solution(object):
    def longestStrChain(self, words):
        dp = {}
        
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in xrange(len(word)):
                posible_predecessor = word[:i]+word[i+1:]
                dp[word] = max(dp.get(word), dp.get(posible_predecessor, 0)+1)
                
        return max(dp.values())

"""
Recursive

Time: O(N^2 x SS),
Basically for every word, check if there are predecessor exist in the words.
If so, keep looking. Until we find the smallest predecessor.
S is the length of each word. isPredecessor takes SS.

Space: O(NS)
"""
class Solution(object):
    def longestStrChain(self, words):
        def isPredecessor(word, word2):
            if not word or not word2: return False
            for i in xrange(len(word)):
                if word[:i]+word[i+1:]==word2:
                    return True
            return False

        def shortestPredecessor(word):
            if word in history: return history[word]
            shortest_predecessor = word
            for word2 in word_group[len(word)-1]:
                if isPredecessor(word, word2):
                    sp = shortestPredecessor(word2)
                    if len(sp)<len(shortest_predecessor): shortest_predecessor = sp
            history[word] = shortest_predecessor
            return history[word]

        word_group = collections.defaultdict(list)
        ans = 1
        history = {} # classic memorization for the recursion.
        
        for word in words:
            word_group[len(word)].append(word)
        
        for l in xrange(max(word_group.keys()), 0, -1):
            if l<ans: break # no need to check since the l is already too small
            for word in word_group[l]:
                ans = max(ans, l-len(shortestPredecessor(word))+1)
        
        return ans


