"""
Does not work with negative values yet.
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans = a^b
        carry = (a&b)<<1
        
        while carry!=0:
            ans, carry = ans^carry, (ans&carry)<<1
            
        return ans