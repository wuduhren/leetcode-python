class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m = m-1 #number of steps need to move down
        n = n-1 #number of steps need to move right
        
        #the total combination of m and n to sort will be (m+n)!
        #since all "move down" are consider the same, we need to remove the repeatition of it sorting: m!.
        #since all "move right" are consider the same, we need to remove the repeatition of it sorting: n!.
        #(m+n)!/m!n!
        
        return math.factorial(m+n)//(math.factorial(m)*math.factorial(n))