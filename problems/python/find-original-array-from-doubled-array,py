"""
Time: O(NLogN)
Space: O(N)
"""
class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed)%2!=0: return []
        
        ans = []
        counter = collections.Counter() #store the count of the doubled number
        count = 0 #sum of count in counter
        
        changed.sort() #need to be sorted, otherwise we cannot identify which number is orginal or it is doubled.
        
        for num in changed:
            if counter[num]>0:
                #num is a doubled num
                counter[num] -= 1
                count -= 1
                ans.append(num/2)
            else:
                #num is an original num
                counter[num*2] += 1
                count += 1
        
        return ans if count==0 else []