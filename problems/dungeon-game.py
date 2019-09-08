"""
First, we define an 2-D matrix `hp`.
`hp[i][j]` is, when entering (i, j), the minimum health required, so that we can reach the princess.

So what is the value of `hp[i][j]`?
At `(i, j)`, we always go to next place where its minimum health required is lowest. (Either `(i+1, j)` or `(i, j+1)`).
And if the value is, for example, `-4` at `(i, j)` the requirement will need to add `4` (`- D[i][j]`).
So the minimum requirement at (i, j) will become:
```
min_required = min(hp[i+1][j], hp[i][j+1]) - D[i][j]
```
Now if `min_required` is smaller or equal to `0`, it means that we don't need any requirement at all, set it to minimum, `1`.
```
hp[i][j] = min_required if min_required>1 else 1
```

Now we only need to work it backward so that we can deduct from the value we are sure.
I add extra row and column to the `hp` and set the bottom and the right of the princess to `1`.
so we don't need to look out for boundaries.
```
hp[N][M-1] = 1
hp[N-1][M] = 1
```

The time complexity is O(NM). Since we only traverse the 2-D matrix twice.
One is for constructing `hp`. The second is calculate the value in `hp`.
The space complexity is O(NM), too.

I learn my anser though [here](https://leetcode.com/problems/dungeon-game/discuss/52826/A-very-clean-and-intuitive-solution-(with-explanation)) which has an awesome explaination, too.
"""
class Solution(object):
    def calculateMinimumHP(self, D):
        N = len(D)
        M = len(D[0])
        hp = [[float('inf')]*(M+1) for _ in xrange(N+1)]
        hp[N][M-1] = 1
        hp[N-1][M] = 1

        for i in reversed(xrange(N)):
            for j in reversed(xrange(M)):
                min_required = min(hp[i+1][j], hp[i][j+1]) - D[i][j]
                hp[i][j] = min_required if min_required>1 else 1
        return hp[0][0]


#Time Limit Exceed
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        def canPass(health_init):
            stack = []

            stack.append((0, 0, health_init))
            while stack:
                i, j, health = stack.pop()
                health_left = health+dungeon[i][j]
                if health<0 or health_left<0: continue
                if i==N-1 and j==M-1: return True
                if i+1<N: stack.append((i+1, j, health_left))
                if j+1<M: stack.append((i, j+1, health_left))

            return False


        N = len(dungeon)
        M = len(dungeon[0])
        l = 0
        h = 0
        for row in dungeon:
            for v in row:
                if v<0:
                    h += -1*v
        while l<h:
            ans = (l+h)/2

            if canPass(ans):
                h = ans
            else:
                l = ans+1
        return l+1

#Time Limit Exceed
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        stack = []
        ans = float('inf')
        N = len(dungeon)
        M = len(dungeon[0])

        stack.append((0, 0, 0, 0))
        while stack:
            i, j, health_curr, health_need = stack.pop()
            health_curr += dungeon[i][j]
            if health_curr<0:
                health_need = max(health_need, -1*health_curr+1)
            if i==N-1 and j==M-1:
                ans = min(ans, health_need)
            if i+1<N: stack.append((i+1, j, health_curr, health_need))
            if j+1<M: stack.append((i, j+1, health_curr, health_need))
        return ans












