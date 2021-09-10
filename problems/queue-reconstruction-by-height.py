"""
Time: O(N^2)
Space: O(N)

People need to be exactly insert to index k, so that there are "exact" k people equal or taller to k.
Shorter person does not matter (invisible) to taller person, so insert taller person first.
People does not care about the people on their right, so insert the person with smaller k first.
"""
class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for h, k in people:
            ans.insert(k, (h, k))
        return ans