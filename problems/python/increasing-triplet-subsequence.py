"""
Time: O(N)
Space: O(1)

Keep updating the minimum element (`min1`) and the second minimum element (`min2`).
When a new element comes up there are 3 possibilities.
0. Equals to min1 or min2 => do nothing.
1. Smaller than min1 => update min1.
2. Larger than min1 and smaller than min2 => update min2.
3. Larger than min2 => return True.
"""
class Solution(object):
    def increasingTriplet(self, nums):
        min1 = min2 = float('inf')
        
        for n in nums:
            if n<min1:
                min1 = n
            elif min1<n and n<min2:
                min2 = n
            elif min2<n:
                return True
        
        return False