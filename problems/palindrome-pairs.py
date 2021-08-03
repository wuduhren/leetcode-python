"""
Time: O(N x L^2), assume the average length of word is L. Note that, eversing the string takes O(L).
Space: O(L), beside from ans, need `left` and `right` constantly to store the word.
"""
class Solution(object):
    def palindromePairs(self, words):
        ans = set()
        index = {word:i for i, word in enumerate(words)}
        
        for i, word in enumerate(words):
            for j in xrange(len(word)+1):
                left = word[:j]
                right = word[j:]
                
                # check if any other word that concat to the left will make palindrome: "OTHER_WORD+`left`+`right`"
                # The above will be palindrome only if
                # 1. `left` is palindrome (left==left[::-1])
                # 2. Exsit an "OTHER_WORD" in word in words that equals to the reverse of `right` (right[::-1] in index and index[right[::-1]]!=i).
                if left==left[::-1]:
                    if right[::-1] in index and index[right[::-1]]!=i:
                        ans.add((index[right[::-1]], i))
                
                # check if any other word that concat to the right will make palindrome: "`left`+`right`+OTHER_WORD"
                # The above will be palindrome only if
                # 1. `rihgt` is palindrome (right==right[::-1])
                # 2. Exsit an "OTHER_WORD" in words that equals to the reverse of `left` (left[::-1] in index and index[left[::-1]]!=i).
                if right==right[::-1]:
                    if left[::-1] in index and index[left[::-1]]!=i:
                        ans.add((i, index[left[::-1]]))
                        
        return ans


"""
Time: O(N^2 x L), will cause TLE.
Space: O(L), can reduce to O(1) by improving isPalindrome()
"""
class Solution(object):
    def palindromePairs(self, words):
        N = len(words)
        ans = []
        
        for i in xrange(N):
            for j in xrange(N):
                if i==j: continue
                if self.isPalindrome(words[i]+words[j]):
                    ans.append([i, j])
        return ans
    
    def isPalindrome(self, word):
        l = 0
        r = len(word)-1
        
        while l<=r:
            if word[l]==word[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
            