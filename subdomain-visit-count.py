#https://leetcode.com/problems/subdomain-visit-count/
class Solution(object):
    def subdomainVisits(self, cpdomains):
        data = collections.Counter()
        return_data = []
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            data[domain]+=count
            
            sub_domain1 = domain.split('.', 1)[-1]
            data[sub_domain1]+=count
            
            if '.' in sub_domain1:
                sub_domain2 = sub_domain1.split('.', 1)[-1]
                data[sub_domain2]+=count
                
        for domain, count in data.items():
            return_data.append(str(count)+' '+domain)
            
        return return_data