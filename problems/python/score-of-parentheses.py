"""
We parse the content in the parentheses and evaluate it.
If the content is empty string then the value is 1.
Otherwise, the value is the value of the content multiply by 2
And we use the exact the same function to evaluate the value of the content (recursion).
We can know the start and the end of the parentheses (so we can extract the content) by `depth`, which is the level of parentheses.

Even though this looks efficient the time complexity is high. O(N^depth).
You can think of a case like this
```
(((((((((( ... content ... ))))))))))
```
Where in every level you have to go through the whole thing again.

The Space complexity is O(depth).
Even we only use O(1) in each function, but the recursion takes stack memory of O(depth).
"""
class Solution(object):
    def scoreOfParentheses(self, S):
        depth = 0
        start = 0
        score = 0
        for i, s in enumerate(S):
            if s=='(': depth+=1
            if s==')': depth-=1
            if depth==0:
                content = S[start+1:i]
                if content == '':
                    score+=1
                else:
                    score+=self.scoreOfParentheses(content)*2
                start = i+1
        return score

"""
If we take a closer look, we will notice that `()` are the only structure that provides value, the outer parentheses just add some multiplier.
So we only need to be concerned with `depth`.
For level we multiply the inner content by 2, so for each `()`, its value is `1 * 2**depth`

The time complexity is O(N).
The space complexity is O(1).
"""
class Solution(object):
    def scoreOfParentheses(self, S):
        score = 0
        depth = 0

        for i, s in enumerate(S):
            if s=='(':
                depth+=1
            else:
                depth-=1
                if S[i-1]=='(':
                    score+=2**depth
        return score
