class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ans = 0
        
        for num in nums:
            isStart = num-1 not in numSet
            if isStart:
                count = 0
                temp = num
                while temp in numSet:
                    count += 1
                    temp += 1
                ans = max(count, ans)
        return ans