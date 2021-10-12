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



class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        def dfs(currSum, k, s=0):
            if k==0: return True
            if currSum==target: return dfs(0, k-1)
            
            for i in xrange(s, N):
                num = nums[i]
                if not visited[i] and num+currSum<=target:
                    visited[i] = True
                    if dfs(currSum+num, k, i+1): return True
                    visited[i] = False
            return False
        
        target, remain = divmod(sum(nums), k)
        if remain>0: return False
        
        N = len(nums)
        visited = [False]*N
        return dfs(target, k)