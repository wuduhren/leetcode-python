"""
Time: O(4^N * N), there are around 4^N of combination. Each taking O(N) to form.
Space: O(N). O(N) for recursion stack. O(N). O(N) for `combination`. O(N+N) ~= O(N).
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(i):
            if i==len(digits):
                ans.append(''.join(combination))
                return
            
            for c in mapping[digits[i]]:
                combination.append(c)
                helper(i+1)
                combination.pop()
        
        mapping = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        
        if not digits: return []
        ans = []
        combination = []
        helper(0)
        return ans