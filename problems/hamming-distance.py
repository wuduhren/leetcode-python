"""
The `^` (XOR) operator returns `1` if the bits are different.
So the main idea is to count the `1` in the `x^y`.
The "easy" way is
```
class Solution(object):
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')
```
This solution takes `O(N)`, `N` is the length of the `bin(x^y)`.

Or we can use some tricks, lets say `A` is `x^y` in binary form.
`A&(A-1)` turns all the bits *right the right-most 1* to 0, including the right-most 1.
```
A = 10110
A = A&(A-1) #10100
A = A&(A-1) #10000
A = A&(A-1) #00000
```
In other words, `A = A&(A-1)` will eliminate a 1 one at a time, starting from right.
Until `A` is all 0.
So we can use this trick to count the `1`.
The run time will be `O(K)`, `K` is the number of 1 in `A`.
"""
class Solution(object):
    def hammingDistance(self, x, y):
        xor = x^y
        count = 0
        while xor:
            count += 1
            xor = xor&(xor-1)
        return count
