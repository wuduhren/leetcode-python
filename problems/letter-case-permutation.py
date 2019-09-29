"""
For each character in the `S` (if it is not a number), it has 2 possibilities, upper or lower.
So starting from an empty string
We explore all the possibilities for the character at index i is upper or lower.

The time complexity is `O(2^N)`.
The space took `O(2^N), too. And the recursion level has N level.
"""
class Solution(object):
    def letterCasePermutation(self, S):
        def dfs(path, i):
            if i>=len(S):
                opt.append(path)
                return
            if S[i] not in num_char:
                dfs(path+S[i].upper(), i+1)
                dfs(path+S[i].lower(), i+1)
            else:
                dfs(path+S[i], i+1)

        num_char = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        opt = []
        dfs('', 0)
        return opt
