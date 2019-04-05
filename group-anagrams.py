#https://leetcode.com/problems/group-anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        
        for string in strs:
            string_count = [0]*26
            a = ord('a')
            for char in string:
                string_count[ord(char)-a] += 1
                
            dic[tuple(string_count)].append(string)
        
        return dic.values()