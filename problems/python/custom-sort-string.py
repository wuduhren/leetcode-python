"""
Take a look at the char in s.
For the char that is in the order, rearrange them to sortedChars with respect to the "order".
For the char that is in not the order, put them in postString.
"""
class Solution(object):
    def customSortString(self, order, s):
        sortedChars = ''
        counter = collections.Counter(s)
        for c in order:
            if c in order:
                sortedChars += c*counter[c]
        
        orderSet = set(order)
        postString = ''
        for c in s:
            if c not in orderSet:
                postString += c
        
        return sortedChars+postString