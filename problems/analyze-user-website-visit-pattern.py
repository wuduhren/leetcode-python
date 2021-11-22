class Solution(object):
    def mostVisitedPattern(self, usernames, timestamps, websites):
        
        data = []
        history = collections.defaultdict(list)
        counter = collections.Counter()
        maxCount = 0
        
        for i in xrange(len(usernames)):
            username = usernames[i]
            timestamp = timestamps[i]
            website = websites[i]
            data.append((timestamp, website, username))
            
        data = sorted(data)
        
        for _, website, username in data:
            history[username].append(website)
        
        for username in history:
            for comb in self.getCombination(history[username]):
                counter[comb] += 1
                maxCount = max(maxCount, counter[comb])
        
        for comb in sorted(counter.keys()):
            if counter[comb]==maxCount: return comb
    
    def getCombination(self, websites):
        def helper(comb, i):
            if len(comb)==3:
                combs.add(tuple(comb[:]))
            elif len(comb)>3 or i>=len(websites):
                return
            else:
                helper(comb+[websites[i]], i+1)
                helper(comb[:], i+1)
                
        combs = set()
        helper([], 0)
        return combs
        

    
        