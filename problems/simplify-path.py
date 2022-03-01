class Solution(object):
    def simplifyPath(self, path):
        ans = ''
        skip = 0
        
        for directory in reversed(path.split('/')):
            if directory=='' or directory=='.':
                continue
            elif directory=='..':
                skip += 1
            else:
                if skip>0:
                    skip -= 1
                    continue
                else:
                    ans = '/'+directory+ans
        
        return ans if ans!='' else '/'