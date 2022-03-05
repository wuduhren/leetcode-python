class Solution(object):
    def removeInvalidParentheses(self, s):
        def dfs(s, curr, i, count):
            if count<0: return
            if len(curr)>self.maxLen: return
            
            if i>=len(s):
                if len(curr)==self.maxLen and count==0:
                    self.ans.append(curr)
                return
            
            if s[i]!='(' and s[i]!=')':
                dfs(s, curr+s[i], i+1, count)
            elif not curr or s[i]!=curr[-1]:
                dfs(s, curr+s[i], i+1, count + (1 if s[i]=='(' else -1))
                dfs(s, curr, i+1, count)
            elif s[i]==curr[-1]:
                dfs(s, curr+s[i], i+1, count + (1 if s[i]=='(' else -1))
                
        def getMaxLen(s):
            openCount = removeCount = 0
            for c in s:
                if c=='(':
                    openCount += 1
                elif c==')':
                    openCount -= 1
                
                if openCount<0:
                    removeCount += abs(openCount)
                    openCount = 0
            removeCount += openCount   
            return len(s)-removeCount
        
        self.ans = []
        self.maxLen = getMaxLen(s)
        
        dfs(s, "", 0, 0)
        return self.ans