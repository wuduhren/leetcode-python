"""
We use `m` to keep track of the min.
The idea is simple, cut the rotated array into half.
One part must be sorted, the other half might or might not be sorted.
In the sorted parted the smallest one is the first element.
In the other part we continue to the same method until it is sorted.
"""
class Solution(object):
    def findMin(self, nums):
        if nums is None or len(nums)==0: return None
        m = nums[0]
        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2
            m = min(m, nums[l], nums[p], nums[r])

            if nums[l]<nums[r]:
                #the l~r is sorted now
                #the smallest is at `l`, and we compared it already.
                break
            else:
                if nums[l]<nums[p]:
                    #l~p is sorted
                    #the smallest is at `l`, and we compared it already.
                    #use the same method on (p+1)~r
                    l = p+1
                elif nums[p]<nums[r]:
                    #p~r is sorted
                    #the smallest is at `l`, and we compared it already.
                    #use the same method on l~(p-1)
                    r = p-1
                else:
                    break
        return m
