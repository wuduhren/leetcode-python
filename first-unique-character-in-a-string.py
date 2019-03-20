#https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, string):
        counter = {}
        
        for char in string:
            if char in counter:
                counter[char]+=1
            else:
                counter[char] = 1
            
        for i in range(len(string)):
            char = string[i]
            if counter[char]==1:
                return i
            
        return -1

"""
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""