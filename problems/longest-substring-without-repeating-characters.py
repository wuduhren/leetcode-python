"""
everytime we iterate to the next char (on index i)
we move the start to the place, where all the char between the start and i are all unique
and keep undating counter til the end

how do we move the start?
we write down the index of the char we last seen
if char is seen, we set the start to (the index we seen char last time)+1
so we don't repeat char, BUT

another rule of start is not moving leftward
bc this will cause more repeating char between start and i
so we have to keep start incremental

we only iterate through the string once so
Time Efficiency is O(N)

we use a dict to keep track of the index of char so
Space Efficiency is O(N)
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s is None or s=='': return 0
        counter = 0 #max length of substring
        start = 0 #index where all the char between the start and i are all unique
        mark = {} #all the char index we last seen

        for i in range(len(s)):
            char_now = s[i]
            if char_now in mark:
                start = max(start, mark[char_now]+1)
            counter = max(counter, i-start+1)
            mark[char_now] = i
                
        return counter