"""
If any element in the triplets is larger than the element in target, it cannot be used.
Check if we have all 3 index found the same value.
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        okIndex = set()
        
        for a, b, c in triplets:
            if a>target[0] or b>target[1] or c>target[2]: continue
            if a==target[0]: okIndex.add(0)
            if b==target[1]: okIndex.add(1)
            if c==target[2]: okIndex.add(2)
        
        return len(okIndex)==3