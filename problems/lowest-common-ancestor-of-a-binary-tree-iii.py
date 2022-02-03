"""
Time: O(H), H is the height of the tree.
Space: O(1)
"""
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        ancestorP = set()
        ancestorQ = set()
        
        temp = p
        while temp:
            ancestorP.add(temp)
            temp = temp.parent
        
        temp = q
        while temp:
            ancestorQ.add(temp)
            temp = temp.parent
        
        commonAncestor = ancestorQ.intersection(ancestorP)
        temp = q
        while temp:
            if temp in commonAncestor: return temp 
            temp = temp.parent
        return None


"""
Time: O(LogN)
Space: O(LogN)

Looking from backward, parents1 and parents2 will be the same at first, since they must have a common ancestor.
Find the last the same parents.
"""
class Solution(object):
    def lowestCommonAncestor(self, p, q):
        parents1 = []
        parents2 = []
        
        curr = p
        while curr:
            parents1.append(curr)
            curr = curr.parent
        
        curr = q
        while curr:
            parents2.append(curr)
            curr = curr.parent
        
        i = len(parents1)-1
        j = len(parents2)-1
        while i>=0 and j>=0 and parents1[i]==parents2[j]:
            i -= 1
            j -= 1
        return parents1[i+1]
    
