class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, target):
            if target==0:
                ans.append(combination.copy())
                return
            
            if i==len(candidates) or candidates[i]>target:
                return
            
            combination.append(candidates[i])
            helper(i+1, target-candidates[i])
            combination.pop()
            
            while i+1<len(candidates) and candidates[i]==candidates[i+1]: i += 1
            helper(i+1, target)
        
        ans = []
        combination = []
        candidates.sort()
        helper(0, target)
        return ans