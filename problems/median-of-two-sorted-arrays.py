"""
On these two sorted arrays (`A` and `B`), we cut both of them into two part, left and right.
`i` is the number of the element on the left of array `A`.
`j` is the number of the element on the left of array `B`.
`M` is the length of `A`.
`N` is the length of `B`.
Imagine if we find the median, and we use the median to seperate all the elements into two sides, left and right.

First, The number of elements on the left must equal to the right. That is:
`Number of elements on the left of A` + `Number of elements on the left of B` is equal to `Number of elements on the right of A` + `Number of elements on the right of B`
Thus `i + j == (M-i) + (N-j)`, so `j = (M+N)/2 - i`

Second, all the elements on the left must be smaller than the median. All the elements on the right must be larger than the median.
The max on the left side of `A` must be <= the min on the right side of `B`.
The max on the left side of `B` must be <= the min on the right side of `A`.
Since both array is sorted, so alreay know
the max on the left side of `A` must be <= to the min on the right side of `A`.
the max on the left side of `B` must be <= the min on the right side of `B`.

For the coding part.
Keep in mind again that **`i` is the number of the element on the left of array `A`.**
And we can use `j = (M+N)/2 - i` to find `j`.
We only need to use binary search to find the right `i` that matches
```python
max_left_A<=min_right_B and max_left_B<=min_right_A
```
And if `min_right_B<max_left_A`, it means that `i` is too large, so we adjust the upper limit of `i`, that is `r = i-1`.
Otherwise it means that `i` is too small, so we adjust the lower limit of `i`, that is `l = i+1`.

Edge cases.
I think this problem is particularly hard because of those complicated edge cases.

[0]
We use the array with smaller length as our `A`.
If not, the `j` might end up being negative.
And we may binary search for fewer time, because `len(A)` is smaller

[1]
What if `M+N` is odd, python will just truncate the float.
If `M+N` is odd, no matter how we choose the median and cut both array into left and right.
There will be one more left. In the `j = (M+N)/2-i` (floor) case, we will put the extra one on the right side.
You may see some other solution using `j = (M+N+1)/2-i` (ceil), in that case, the extra one will be on the left side.
So when `M+N` is odd using `j = (M+N)/2-i` the answer will be `min(min_right_A, min_right_B)`
And using `j = (M+N+1)/2-i`, the anser will be `max(max_left_A, max_left_B)`

[2]
There will be cases we end up `i == 0` (0 element on the left side of `A`), so we see it as the last element on the left side of `A` is negative infinity.
There will be cases we end up `M-i == 0` (0 element on the right side of `A`), so we see it as the first element on the right side of `A` is infinity.

The time complexity is O(Log(min(M, N))).

"""
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        if len(A)>len(B): A, B = B, A #[0]

        M, N = len(A), len(B)
        l, r = 0, M

        while l<=r:
            i = (r+l)/2
            j = (M+N)/2-i #[1]

            max_left_A = A[i-1] if i>0 else float('-inf') #[2]
            max_left_B = B[j-1] if j>0 else float('-inf')

            min_right_A = A[i] if M-i>0 else float('inf')
            min_right_B = B[j] if N-j>0 else float('inf')

            if max_left_A<=min_right_B and max_left_B<=min_right_A:
                if (M+N)%2==0:
                    return (max(max_left_A, max_left_B)+min(min_right_A, min_right_B))/2.0
                else:
                    return min(min_right_A, min_right_B) #[1]
            elif min_right_B<max_left_A:
                r = i-1
            else:
                l = i+1
        return None















































class Solution(object):
    def findMedianSortedArrays(self, X, Y):
        if len(X)>len(Y): X, Y = Y, X
        M, N = len(X), len(Y)

        after = (M+N-1)/2
        l, r = 0, M

        while l<r:
            i = (l+r)/2
            if after-i-1 < 0 or X[i] >= Y[after-i-1]:
                r = i
            else:
                l = i + 1
        i = l
        nextfew = sorted(X[i:i+2] + Y[after-i:after-i+2])
        return (nextfew[0]+nextfew[1-(M+N)%2])/2.0
