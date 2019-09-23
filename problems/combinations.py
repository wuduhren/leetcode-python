class Solution(object):
    def combine(self, N, K):
        def helper(first, combination):
            if len(combination)==K:
                answer.append(combination)
            else:
                for num in xrange(first, N+1):
                    helper(num+1, combination+[num])
        answer = []
        helper(1, [])
        return answer
"""
`helper()` helps append `combination` to the `answer` if there are already K element in the `combination`.

The parameter `first` means we are only going to use number fisrt~N.
Because we used the smaller number already, or we will have duplicates.

If there are not enough element in the `combination`, it will run through fisrt~N and append all the element `num` to the `combination`, and set the `first` to num+1.
In other words, if we use 3, we will not use 3 and the number below 3 anymore.

The call stack will be
```
N = 4, K = 2.

helper(1, [])
    helper(2, [1])
        helper(3, [1, 2])
        helper(4, [1, 3])
        helper(5, [1, 4])

    helper(3, [2])
        helper(4, [2, 3])
        helper(5, [2, 4])

    helper(4, [3])
        helper(5, [3, 4])

    helper(5, [4])
```
"""

class Solution(object):
    def combine(self, N, K):
        answer = []
        combination = []
        first = 1
        while True:
            if len(combination)==K:
                answer.append(combination[:])

            if len(combination)==K or first>N:
                if not combination: return answer
                first = combination.pop()+1 #backtrack
            else:
                combination.append(first)
                first+=1
"""
Iterative solution is not so easy to understand.
I suggest you run a easier example on paper, and you will know how it works. (`N = 4 , K = 2`)
For every iterative, we append the combination to the answer if the length is equal to K already.
Adjust the `first` whenever needed (`len(combination)==K or first>N`), if not, keep on appending.

The time complexity is O(N!/(N!(N-K)!)), combination N choose K.
The space complexity is O(N!/(N!(N-K)!)), combination N choose K.
"""



#DFS
class Solution(object):
    def combine(self, N, K):
        def dfs(n_min, path):
            if len(path)==K:
                opt.append(path)
                return
            else:
                for n in xrange(n_min, N+1):
                    dfs(n+1, path+[n])
        opt = []
        dfs(1, [])
        return opt








