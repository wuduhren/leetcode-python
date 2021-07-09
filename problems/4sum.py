"""
Time: O(N^3)
Space: O(1)

Using tuple to remove redundant, each `ans.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))` is using constant time and space.
So no increase to the time and space complexity.
"""
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        N = len(nums)
        ans = set()
        
        for a in xrange(N):
            for b in xrange(a+1, N):
                c = b+1
                d = N-1
                
                while c<d:
                    s = nums[a]+nums[b]+nums[c]+nums[d]
                    
                    if s>target:
                        d -= 1
                    elif s<target:
                        c += 1
                    else:
                        ans.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
                        d -= 1
                        c += 1
        return ans

"""
Remove tuple by skipping the same value for each a, b, c and d.
I find that doing this does not improve overall run time.
"""
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        N = len(nums)
        ans = []
        
        for a in xrange(N):
            if a>0 and nums[a]==nums[a-1]: continue
            for b in xrange(a+1, N):
                if b>0 and nums[b]==nums[b-1] and a!=b-1: continue
                c = b+1
                d = N-1
                
                while c<d:
                    s = nums[a]+nums[b]+nums[c]+nums[d]
                    
                    if s>target:
                        d -= 1
                    elif s<target:
                        c += 1
                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        
                        while c<d and nums[c]==nums[c+1]: c+=1
                        while c<d and nums[d]==nums[d-1]: d-=1
                        
                        d -= 1
                        c += 1
        return ans