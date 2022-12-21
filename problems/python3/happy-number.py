class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSquare(n) -> int:
            ans = 0
            while n>0:
                ans += (n%10)**2
                n = n//10
            return ans

        visited = set()
        visited.add(1)

        while n not in visited:
            visited.add(n)
            n = digitSquare(n)

        return n==1
