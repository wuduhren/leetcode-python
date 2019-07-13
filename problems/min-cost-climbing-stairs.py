"""
First setup a memo.
Every value on index i on the memo, is the min cost we are going to get there.
In this case, we are trying to get the min cost going to the 'top'.
For every i, we either comes from i-1 or i-2
* If we come from i-1, the cost to get to i is memo[i-1]+cost[i-1] (the min cost to go to i-1) + (the cost on i-1)
* If we come for i-2, the cost to get to i is memo[i-2]+cost[i-2] (the min cost to go to i-2) + (the cost on i-2)

We pick the min from these two option.
And continue to iterate to the end.
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        if cost is None or len(cost)==0: return 0
        memo = [0]*(len(cost)+1)
        
        for i in xrange(len(memo)):
            if i==0 or i==1:
                memo[i] = 0
            else:
                memo[i] = min(memo[i-1]+cost[i-1], memo[i-2]+cost[i-2])
                
        return memo[-1]