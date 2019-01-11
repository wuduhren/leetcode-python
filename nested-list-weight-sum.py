#https://leetcode.com/problems/nested-list-weight-sum/
class Solution(object):
    #DFS(Depth-First-Search)
	#Efficiency: O(N), Space: O(D).
	#N is the total element of the nestedList, D is the depth.
    def depthSum(self, nestedList, weight=1):
        counter = 0
        for e in nestedList:
            if e.isInteger():
                counter+=(e.getInteger()*weight)
            else:
                counter+=self.depthSum(e.getList(), weight+1)
        return counter
    
    #BFS(Breadth-First-Search)
	#Efficiency: O(N), Space: O(N).
    def depthSum(self, nestedList):
        counter = 0
        queue = [(1, e) for e in nestedList]
        while queue:
            weight, e = queue.pop(0)
            if e.isInteger():
                counter += e.getInteger()*weight
            else:
                for child_list in e.getList():
                    queue.append((weight+1, child_list))
                
        return counter