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