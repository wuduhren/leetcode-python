"""
Time: O(N)
Space: O(N) for creating the list preorder.split(',')
"""
class Solution(object):
    def isValidSerialization(self, preorder):
        slot = 1
        
        for c in preorder.split(','):
            slot -= 1 #each elemet consumes a slot
            if slot<0: return False
            if c!='#': slot += 2 #each non-null node also create 2 slot
            
        return slot==0 #all slots should be fill