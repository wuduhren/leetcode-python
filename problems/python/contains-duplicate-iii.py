"""
Time: O(N)
Space: O(K)

Imagine there are several different buckets. Each bucket can only contain one number.
Bucket1 contains a number within [0, t]
Bucket2 contains a number within [t+1, 2t+1]
Bucket3 contains a number within [2t+2, 3t+2]
...

For each num, put it in the bucket.
Before that.
If the bucket is already occupied, there must be another num that "abs(anotherNum - num) <= t", return True.
Check the neighbor buckets, the number within those might also "abs(anotherNum - num) <= t". If so, return True.

We only consider k numbers before num.
So remove nums[i-k-1] from the bucket if we already have k elements in the buckets.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        bucket = {}
        
        for i, num in enumerate(nums):
            if len(bucket)>k:
                bidToRemove = nums[i-k-1]//(t+1)
                del bucket[bidToRemove]
            
            bid = num//(t+1)
            if bid in bucket: return True
            if bid+1 in bucket and abs(bucket[bid+1]-num)<=t: return True
            if bid-1 in bucket and abs(bucket[bid-1]-num)<=t: return True
            bucket[bid] = num
        
        return False