"""
Time: O(N^2 * M). N is the length of the s. M is the number of word in wordDict.
Note that s[i:i+len(word)]==word takes O(N) time.

Space: O(N) for the recursion memory stack size.

dfs(i) := will return starting at index i, if i to the end the string can be separated.
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i==len(s): return True
            if i in history and not history[i]: return False
            
            for word in wordDict:
                if i+len(word)<=len(s) and s[i:i+len(word)]==word:
                    history[i] = True
                    if dfs(i+len(word)): return True
            history[i] = False
            return False
        
        history = {}
        return dfs(0)