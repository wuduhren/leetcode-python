"""
This answer is the python version of the offical answer.

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def nextPermutation(self, nums):
        def reverse(start):
            end = len(nums)-1
            
            while start<end:
                swap(start, end)
                start += 1
                end -= 1
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        
        i = len(nums)-2
        
        while i>=0 and nums[i+1]<=nums[i]:
            i -= 1
        
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]: j -= 1
            swap(i, j)
        
        reverse(i+1)
        return nums

"""
Next Permutation means find the next (slightly) larger number using nums.

1. Iterate from right, find the first num that is smaller. That's the one we are going to swap. => nums[i]
2. From the nums right to nums[i], find the smallest num that is larger than nums[i] => nums[j]
Since the right of the i must be an increasing sequence (looking from right), the first one that larger than nums[i] is the smallest one that is larger than nums[i]
3. Swap nums[i] and nums[j]
4. sort nums[i+1:] it will be the smallest permutaion.
5. Note that when an list is in increasing order looking from right, we can use `reverse` to sort it.
"""
class Solution(object):
    def nextPermutation(self, nums):
        def reverse(nums, l, r):
            while l<=r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            
        i = len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]: i -= 1 #[1]
        
        if i==-1:
            return reverse(nums, 0, len(nums)-1) #nums is the largest permutation, sort nums
        else:
            j = len(nums)-1
            while j>i and nums[j]<=nums[i]: j -= 1 #[2]
            nums[i], nums[j] = nums[j], nums[i] #[3]
            reverse(nums, i+1, len(nums)-1) #[4]