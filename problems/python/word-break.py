class Solution(object):
    def wordBreak(self, s, wordDict):
        def helper(s_left):
            if not s_left: return True
            if s_left in history: return history[s_left]
            
            for word in wordDict:
                if len(s_left)<len(word): continue
                if s_left[:len(word)]==word and helper(s_left[len(word):]):
                    history[s_left] = True
                    return history[s_left]
            
            history[s_left] = False
            return history[s_left]
        
        history = {}
        return helper(s)