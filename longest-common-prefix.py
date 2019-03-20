#https://leetcode.com/problems/longest-common-prefix/
class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0 or strs==None:
            return ''
        
        bench_mark = strs[0]
        
        for i in range(1, len(bench_mark)+1):
            common_substring = bench_mark[:i]
            for s in strs:
                if s[:i]!=common_substring:
                    if i==1:
                        return ''
                    else:
                        return bench_mark[:i-1]
        return bench_mark

"""
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""