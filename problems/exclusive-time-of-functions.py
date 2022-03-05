class Solution(object):
    def exclusiveTime(self, n, logs):
        ans = [0]*n
        data = []
        for log in logs:
            fid, action, t = log.split(':')
            data.append([int(t), -1 if action=='start' else 1, int(fid)])
        
        data.sort()
        
        stack = []
        for t, action, fid in data:
            if action==-1:
                if stack:
                    prevT, _, prevFid = stack[-1]
                    ans[prevFid] += t-prevT
            elif action==1:
                prevT, _, prevFid = stack.pop()
                ans[fid] += t+1-prevT
                if stack: stack[-1][0] = t+1
                
            if action==-1: stack.append([t, action, fid])
        
        return ans