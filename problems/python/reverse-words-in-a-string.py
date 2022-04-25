"""
I see space as the end of a word.
If a word end I will add it to the left of the output.
That is why I have to add an extra space to the original 's' [0]
Be careful There may be continuous space or space at the start and the end. [1]
The way we combine string, there will be an extra space at the end, so I remove it. [2]

Time complexity is O(N).
Because we loop through the stirng once.

Space complexity is O(N).
Because we use 'opt' to store the output.
"""
class Solution(object):
    def reverseWords(self, s):
        temp = ''
        opt = ''
        s = s+' ' #[0]
        for c in s:
            if c==' ':
                if temp is not '': opt = temp+' '+opt #[1]
                temp = ''
            else:
                temp+=c

        opt = opt[:-1] #[2]
        return opt



class Solution(object):
    def reverseWords(self, s):
        stack = s.split()
        
        ans = ''
        while stack: ans += stack.pop()+' '
        ans = ans[:len(ans)-1] #remove last space
        return ans