"""
Time: O(N^K), assuming the number of element in the combination that sums up to "target" is K.
For each element, there is N choices.
Which means the number of combination is N*N*N... for K times.
~= O(N^K)

Space: O(K)

K is approximate to target/min(candidates).
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, currSum, target):
            if currSum>target:
                return
            
            if currSum==target:
                ans.append(combination.copy())
                return
            
            for j in range(i, len(candidates)):
                combination.append(candidates[j])
                helper(j, currSum+candidates[j], target)
                combination.pop()
                
        ans = []
        combination = []
        helper(0, 0, target)
        return ans