class Solution(object):
    def kthSmallest(self, matrix, k):
        memo = [0]*len(matrix)
        opt = []
        while len(opt)<k:
            m = float('inf')
            i_min = None
            for i, row in enumerate(matrix):
                if memo[i]<len(matrix) and row[memo[i]]<m:
                    m = row[memo[i]]
                    i_min = i
            opt.append(m)
            memo[i_min]+=1
        return opt[-1]

"""
Time: O(kN).
Space: O(kN)
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        def count_smaller(t):
            count = 0
            col = 0
            for i, row in enumerate(reversed(matrix)):
                while col<len(row) and row[col]<=t:
                    count += len(matrix)-i
                    col += 1
            return count
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        
        while l<r:
            m = (l+r)/2
            c = count_smaller(m)
            
            if c<k:
                l = m+1
            else:
                r = m
                
        return l

"""
Time: O(NLOG(max-min))
"""