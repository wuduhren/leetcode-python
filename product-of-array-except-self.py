"""
I learn the solution from hqpdash and c040120's answer

the main idea is for each element of the array 
to get the product from all its left and the product from all its right
then we product those two

note that the first element of nums don't have any left element
so for the output[0], it is 1*(the product of all its right)
the last element of nums don't have any right element
so for the output[last], it is 1*(the product of all its left)

first, we iterate through every element [1]
the main gaol here is to produce an array that
output[i] is the product of all nums[i]'s left
by incrementally product every number we gone through and store it in 't' [2]

second, we iterate backward [3]
the main gaol here is to get the product from all nums[i] right and store it in 't' [4]
and product it with the output from first step
so output[i] now is (the product of all nums[i]'s left) * (the product of all nums[i]'s right) [5]
"""

class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        output = []

        t = 1
        for i in xrange(l): #[1]
            output.append(t)
            t = t*nums[i] #[2]
        
        t = 1 #reset the temporary variable
        for i in reversed(xrange(l)): #[3]
            output[i] = output[i]*t #[5]
            t = t*nums[i] #[4]
            
        return output