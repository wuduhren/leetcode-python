class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        ans = []
        
        counter = collections.Counter()
        
        for num in list(set(nums1)):
            counter[num] += 1
        for num in list(set(nums2)):
            counter[num] += 1
        for num in list(set(nums3)):
            counter[num] += 1
        
        for num in counter:
            if counter[num]>=2: ans.append(num)
        
        return ans