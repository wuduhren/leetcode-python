"""
dp[i] := number of envelopes that envelopes[i] can contains the most.
Very similar to LIS problem (Leetcode 300)
This method will get TLE

Time: O(N^2)
Space: O(N)
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes: return 0
        
        N = len(envelopes)
        dp = [1]*N
        envelopes = sorted(envelopes)
        ans = 1
        
        for i in xrange(N):
            for j in xrange(i):
                if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    ans = max(ans, dp[i])
        
        return ans

"""
dp[i] := the smallest ending number of a sequence that has length i+1
First, sort the envelopes by width. (envelope[0])
Second, return the LIS of heights ([envelope[1] for envelope in envelopes]).
This automatically gets the number of "russian dolls".

However, we might choose [3,4], [3,7] as a valid solution. This is not correct because w1==w2.
So we do a quick fix by sorting the envelopes with w and h reversed.
So that getLIS() will not choose [3,4], [3,7]

Time: O(NLogN)
Space: O(N)
"""
import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes: return 0
        
        N = len(envelopes)
        dp = [1]*N
        envelopes = envelopes.sort(key=lambda x:(x[0], -x[1]))

        return self.getLIS([envelope[1] for envelope in envelopes])
    
    def getLIS(self, A):
        dp = []

        for n in A:
            i = bisect.bisect_left(dp, n)

            if i==len(dp):
                dp.append(n)
            else:
                dp[i] = n
        
        return len(dp)
