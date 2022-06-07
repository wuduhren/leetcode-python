"""
`helper(i)` finds all the palindrome substring from i to j see if we can get an answer by recursively calling `helper(j+1)`.

Time: O(2^N * N), for a string length S, there will be 2^N combination of substrings. For each substring, it will take O(N) to test if they are all palindrome.
Space: O(N). `partition` will takes O(N) and recursion stack will also take O(N). O(N + N) ~= O(N)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(i):
            if i>=len(s):
                ans.append(partition.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    partition.append(s[i:j+1])
                    helper(j+1)
                    partition.pop()

        def isPalindrome(i, j):
            while i<=j:
                if s[i]!=s[j]: return False
                i += 1
                j -= 1
            return True
                
        ans = []
        partition = []
        helper(0)
        return ans

"""
If you look closely you can see that we execute `isPalindrome` on many repeated substrings.
We can optimize this by storing the result in `dp` and reuse it.
Since all the less difference i and j (shorter substring s[i:j+1]) will be process first in the `isPalindrome`.
When checking if s[i:j+1] is a palindrome or not, we can simply check the if s[i]==s[j] and the previous result (dp[i+1][j-1])

Time: O(2^N * N), The overall time complexity is the same, but isPalindrome is actually a lot faster.
Space: O(N^2) for `dp`.
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(i):
            if i>=N:
                ans.append(partition.copy())
                return
            
            for j in range(i, N):
                if isPalindrome(i, j):
                    partition.append(s[i:j+1])
                    helper(j+1)
                    partition.pop()

        def isPalindrome(i, j):
            dp[i][j] = i==j or (j-i==1 and s[i]==s[j]) or (s[i]==s[j] and dp[i+1][j-1]) #len==1 palindrome or len==2 palindrome or len>=3 palindrome
            return dp[i][j]
        
        N = len(s)
        ans = []
        partition = []
        dp = [[False]*N for _ in range(N)]

        helper(0)
        return ans