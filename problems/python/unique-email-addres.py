#https://leetcode.com/problems/unique-email-addresses/
"""
[0]
First we use set to store the processed email
set is implement in hashmap, so it takes O(1) to store unique value.

[1]
Split the email by '@' to local_name and domain_name

[2]
we find the first '+' and remove the char after it.

[3]
we remove the '.' in the string.

we iterate the local_name part 3 times
first time we are finding the first '@'
second time we are finding the first '+'
third time we are finding all the '.'

isn't faster to just iterate once?
so I come up with the second solution which only iterate once to process the email
but it is slower, I guess Python really do a good job on the string function
because they are implemented by C.
in other language, the second solution might be faster.

both solution are O(N)
"""
class Solution(object):
    def numUniqueEmails(self, emails):
        book = set() #[0]
        for s in emails:
            at = s.find('@') #[1]
            local_name = s[:at]
            domain_name = s[at:]
            
            plus = local_name.find('+') #[2]
            if plus!=-1: local_name = local_name[:plus]

            local_name = local_name.replace('.', '') #[3]

            r = local_name+domain_name #[0]
            book.add(r)
            
        return len(book)


class Solution(object):
    def numUniqueEmails(self, emails):
        book = set()
        for email in emails:
            r = ''
            ignore = False
            for i, c in enumerate(email):
                if c=='@':
                    r+=email[i:]
                    break
                    
                if ignore: continue
                    
                if c=='.':
                    continue
                elif c=='+':
                    ignore = True
                else:
                    r+=c                    
            book.add(r)
        return len(book)


