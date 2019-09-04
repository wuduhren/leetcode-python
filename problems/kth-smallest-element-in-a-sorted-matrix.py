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
