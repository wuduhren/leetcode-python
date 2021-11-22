class Solution(object):
    def numIslands2(self, m, n, positions):
        ans = []
        uf = UnionFind(m*n)
        
        for x, y in positions:
            i = x*n+y
            if uf.isLand(i):
                ans.append(uf.count)
                continue
            
            connected = []
            if (x-1>=0 and uf.isLand((x-1)*n+y)): connected.append((x-1)*n+y)
            if (x+1<m and uf.isLand((x+1)*n+y)): connected.append((x+1)*n+y)
            if (y-1>=0 and uf.isLand(x*n+y-1)): connected.append(x*n+y-1)
            if (y+1<n and uf.isLand(x*n+y+1)): connected.append(x*n+y+1)
            
            
            uf.setLand(i)
            for nei in connected: uf.union(nei, i)
            ans.append(uf.count)
        
        return ans
            
class UnionFind(object):
    def __init__(self, N):
        self.count = 0
        self.parents = [-1]*N
        self.ranks = [0]*N
        
    def isLand(self, i):
        return self.parents[i]>=0
    
    def setLand(self, i):
        self.parents[i] = i
        self.count += 1
    
    def find(self, i):
        if self.parents[i]!=i: self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i1, i2):
        parent1 = self.find(i1)
        parent2 = self.find(i2)
        
        if parent1!=parent2:
            if self.ranks[parent1]>self.ranks[parent2]:
                self.parents[parent2] = parent1
            elif self.ranks[parent1]<self.ranks[parent2]:
                self.parents[parent1] = parent2
            else:
                self.parents[parent1] = parent2
                self.ranks[parent2] += 1
                
            self.count -= 1
    