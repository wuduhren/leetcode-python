"""
Reversing a string is equivalent to
Switch the first and the last, the second and the second last, the third and the third last...
So I use two pointers, 's' at the start, 'e' at the end.
If e and s collapse, the proccess is finished.

(a, b) = (b, a) is equal to

temp = a
a = b
b = temp

For time complexity is O(N), N is the length of the string.
Space complexity is O(1), because I only use pointers and a space to store one char.
"""
class Solution(object):
    def reverseString(self, string):
        s = 0
        e = len(string)-1
        while e>s:
            (string[s], string[e]) = (string[e], string[s])
            s+=1
            e-=1
        return string
