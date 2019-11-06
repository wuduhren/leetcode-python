class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        def search(subs):
            if not nums: return True
            n = nums.pop()
            for i, sub in enumerate(subs):
                if sub+n<=target:
                    subs[i]+=n
                    if search(subs): return True
                    subs[i]-=n
                if not sub: break
            nums.append(n)
            return False

        if sum(nums)%k!=0: return False
        target = sum(nums)/k
        nums.sort()
        return search([0]*k)
