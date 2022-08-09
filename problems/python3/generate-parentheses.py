class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(parentheses, left, right):
            if len(parentheses)==n*2:
                ans.append("".join(parentheses))
                return
            
            if left<n:
                parentheses.append('(')
                helper(parentheses, left+1, right)
                parentheses.pop()
            
            if left>right:
                parentheses.append(')')
                helper(parentheses, left, right+1)
                parentheses.pop()
        
        ans = []
        helper([], 0, 0)
        return ans