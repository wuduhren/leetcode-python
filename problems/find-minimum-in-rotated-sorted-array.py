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



"""
Pointer l and r is at the start and at the end of the list. [0]
We only consider the numbers between l and r.

If the list is already sorted, return the left most element. [1]

Now, we cut the rotated array into half. l~m and m~r.
Normally, one part will be sorted, the other half is not.
The min must be in the unsorted part.
So we move the pointer and do the same thing on the unsorted part. [2]

One scenario to consider is that the cutting point, m, being the smallest element.
This will cause both l~m and m~r to both be sorted.
So we need to check it. [3]

Time: O(LogN)
Space: O(1)
"""

class Solution(object):
    def findMin(self, nums):
        if not nums: return 0
        l = 0 #[0]
        r = len(nums)-1 #[0]

        while l<=r:
            if nums[l]<=nums[r]: return nums[l] #[1]
            
            m = (l+r)/2
            if m-1>=0 and nums[m-1]>nums[m]: return nums[m] #[3]
            
            if nums[l]<=nums[m]:
                l = m+1 #[2]
            else:
                r = m-1 #[2]
        return 0