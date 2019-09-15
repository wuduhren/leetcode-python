"""
If all the numbers in the array is larger or equal than 0, all the square value will automatically be sorted.

If there are negatives in the array, we need to seperate the negatives and the others.
To do that, we need to find the index of 0 or index of first positive element. We call the index `m`.
So for the non-negative part, it is sorted already: `numbers[m:]`.
The negative part sorted: `[-1*n for n in reversed(numbers[:m])]`

And now we apply the merge method in the merge sort.
The method takes two sorted array and turn it into one.
If you are not familiar it take a look at [this](https://leetcode.com/problems/merge-sorted-array/discuss/208832/Python-O(M%2BN)-Solution-Explained).
After we got the sorted array, we compute all the squares and return.

The time complexity is O(N).
The space complexity is O(N).
"""
class Solution(object):
    def sortedSquares(self, numbers):
        if not numbers: return numbers

        if numbers[0]>=0:
            return [n**2 for n in numbers]

        m = 0
        for i, n in enumerate(numbers):
            if n>=0:
                m = i
                break

        A, B = numbers[m:], [-1*n for n in reversed(numbers[:m])]
        return [n**2 for n in self.merge(A, B)]

    def merge(self, A, B):
        a = b = 0
        opt = []
        while a<len(A) and b<len(B):
            if A[a]<B[b]:
                opt.append(A[a])
                a+=1
            else:
                opt.append(B[b])
                b+=1
        if a<len(A): opt.extend(A[a:])
        if b<len(B): opt.extend(B[b:])
        return opt

"""
How to approach problem like this?

**Mindset 1, think of the time complexity of your brute force.**
In this case, simply square all the element and sort them.
That is O(NLogN).
So we are going to try to reduce it into O(N) or O(LogN) or O(1).

**Mindset 2, think of the time complexity that you are not able to reduce.**
For example, I could not think of a way to square all the sorted element without O(N).
So all other operation less or equal to O(N) does not effect the time complexity.
When I am trying to find `m`, I can use binary search to search for it, the time complexity is O(LogN).
But O(N) is fine, so I use this simpler approach.
Sure, we can optimize it and make it faster. But it is not the bottle neck here.
**I think what the interviwer wanted to see is you realizing the bottle neck and solve it.**
"""
