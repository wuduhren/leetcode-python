#https://leetcode.com/problems/longest-common-prefix/
"""
We ramdomly pick a string from 'strs' as 'bench_mark' [0]
Lets say the 'bench_mark' is 'flower'
We compair 'f', 'fl', 'flo'... to every other string [1]
If any string does not match, we return the longest common prefix [2]
In ths case the whole 'bench_mark' is actually the longest common prefix [3]
We need to return the 'bench_mark'


"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0 or strs==None:
            return ''
        
        bench_mark = strs[0] #[0]
        
        for i in range(1, len(bench_mark)+1): #[1]
            common_substring = bench_mark[:i]
            for s in strs:
                if s[:i]!=common_substring: #[2]
                    return bench_mark[:i-1]
        return bench_mark #[3]