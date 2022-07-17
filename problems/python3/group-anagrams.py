class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def normalize(string: str) -> str:
            counter = collections.Counter()
            ans = ''
            
            for c in string:
                counter[c] += 1
            
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if counter[c]>0:
                    ans += c+str(counter[c])
            return ans
                    
        group = collections.defaultdict(list)
        ans = []
        
        for string in strs:
            group[normalize(string)].append(string)
        
        for normalizedString in group:
            ans.append(group[normalizedString])    
        return ans