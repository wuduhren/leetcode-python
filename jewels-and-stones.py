#https://leetcode.com/problems/jewels-and-stones/
class Solution(object):
    def numJewelsInStones(self, J, S):
        n=0
        for j in J:
            n+=S.count(j)
        return n