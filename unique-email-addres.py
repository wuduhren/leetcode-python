#https://leetcode.com/problems/unique-email-addresses/
import re
class Solution(object):
    def numUniqueEmails(self, emails):
        rs_list = []
        for s in emails:
            local_name = s[:s.index('@')]
            domain_name = s[s.index('@'):]
            
            local_name = local_name[:local_name.index('+')]
            local_name = local_name.replace('.', '')
            r = local_name+domain_name
            
            if r not in rs_list:
                rs_list.append(r)
        return len(rs_list)