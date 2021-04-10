class Solution(object):
    def knightDialer(self, n):
        def helper(initial, n):
            # return the number of posible count starting from initial with n steps left
            
            if str(initial)+'-'+str(n) in history: return history[str(initial)+'-'+str(n)]
            count = 0
            
            if n==0: return 1
            for next_number in memo[initial]:
                count += helper(next_number, n-1)
            
            history[str(initial)+'-'+str(n)] = count
            return count
        
        memo = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        history = {}
        count = 0

        for i in xrange(10):
            count += helper(i, n-1)
        return count % 1000000007

"""
dp[n][i] := number of ways to ends at number i after n moves.

Time: O(N).
Space: O(N). Can reduce to O(1).
"""
class Solution(object):
    def knightDialer(self, n):
        dp = [[0 for _ in xrange(10)] for _ in xrange(n)]
        for i in xrange(10): dp[0][i] = 1 #initialize
        
        memo = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

        for j in xrange(n-1):
            for i in xrange(10):
                for next_n in memo[i]:
                    dp[j+1][next_n] += dp[j][i]
        
        return sum(dp[n-1]) % 1000000007