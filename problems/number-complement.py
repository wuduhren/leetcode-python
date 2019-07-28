"""
First, we convert the num to its birary.
```
>>> bin(5)
>>> '0b101'
```

Second, we need to return the base10 of binary's the complement.
Complement is easy `'101' => '010'`.
Turn to base10:
```
'010' => 0*pow(2, 2) + 1*pow(2, 1) + 0*pow(2, 0)
'11011' => 1*pow(2, 4) + 1*pow(2, 3) + 0*pow(2, 2) + 1*pow(2, 1) + 1*pow(2, 0)
```

Basics bit manipulation.
<https://www.youtube.com/watch?v=NLKQEOgBAnw>
"""
class Solution(object):
    def findComplement(self, num):
        b = bin(num)[2:]
        opt = 0
        for i, c in enumerate(reversed(b)):
            if c=='0': opt+=pow(2, i)
        return opt
