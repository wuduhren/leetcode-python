"""
`l` and `r` are the points on width that form the area.
The height on `l` is `H[l]` and `r` is `H[r]`.
The area that form by `l` and `r` is `(r-l)*min(H[r], H[l])`.

We are going to calculate the area everytime we move `l` or `r`.
And maintain the `ans`, which is the max of all area.

Now, we put `l` and `r` at the beginning and at the end of the array.
We calculate the area and update `ans`, move `l` or `r` inward.
How are we going to find a larger area with shorter width that form by `l` and `r`?
The answer is, we move the `l` or `r` with shorter `H[l]` or `H[r]`, so we might get a larger `min(H[r], H[l])`, which leads to possibly larger area.

By doing this, we now have a new pair of `l` and `r`.
We calculate the area and update `ans`, move `l` or `r` inward.

...

We repeat the process until `l` and `r` collapse.
So by repeatedly moving `l` and `r` inward, we can run through all the shorter width that might form area larger than `ans`.
"""
class Solution(object):
    def maxArea(self, H):
        r, l = len(H)-1, 0
        ans = float('-inf')

        while r>l:
            ans = max(ans, (r-l)*min(H[r], H[l]))
            if H[r]>H[l]:
                l = l+1
            else:
                r = r-1
        return ans


class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        ans = 0
        
        while i<j:
            ans = max(ans, min(height[i], height[j])*(j-i))
            if height[i]<height[j]:
                """
                If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line.
                """
                i += 1
            else:
                j -= 1
        return ans