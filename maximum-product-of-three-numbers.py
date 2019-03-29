"""
if we sort the array, the max would be the product 3 numbers on the right.
but if there are negative numbers, it could also be possible that
two negative numbers lying at the left extreme end could also contribute to lead to a larger product.
thus, after sorting, either

max1 * max2 * max3
max1 * min1 * min2

so our gaol will be to find the max 3 numbers and min 2 numbers in the array
"""
class Solution(object):
    def maximumProduct(self, nums):
        min1 = float('inf') #smallest
        min2 = float('inf') #second smallest

        max1 = float('-inf') #largest
        max2 = float('-inf') #second largest
        max3 = float('-inf') #third largest

        for n in nums:
            if n<=min1:
                min2 = min1
                min1 = n
            elif n<=min2:
                min2 = n
            
            if n>=max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n>=max2:
                max3 = max2
                max2 = n
            elif n>=max3:
                max3 = n

        return max(min1*min2*max1, max1*max2*max3)