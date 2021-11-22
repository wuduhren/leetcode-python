class Solution(object):
    def numPairsDivisibleBy60(self, times):
        counter = collections.Counter()
        ans = 0
        
        for time in times:
            time = time%60
            ans += counter[60-time if time!=0 else 0]
            counter[time] += 1
    return ans