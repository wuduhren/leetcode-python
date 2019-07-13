"""
i1 and i2 is the pointer we point to the starting point.
Character before i1 and i2 we already processed.
When they are set to -1, the whole string are already processed.

#for-loop can't find the '.' any more. [0]

after two version is fully processed and couldn't find which is larger, return 0. [1]

Time Complexity is O(N).
N is the length of those version, because we potentially loop through them once.

Space Complexity is O(1).
Because we only store two pointers and two integer.
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        def getVersion(version, start):
            if start==-1: return 0, -1
            for i in xrange(start, len(version)):
                if version[i]=='.':
                    return int(version[start:i]), i+1
            return int(version[start:]), -1 #[0]
            
        i1 = i2 = 0
        
        while True:
            sub_version1, i1 = getVersion(version1, i1)
            sub_version2, i2 = getVersion(version2, i2)
            
            if sub_version1>sub_version2:
                return 1
            elif sub_version1<sub_version2:
                return -1
            elif i1==-1 and i2==-1: #[1]
                return 0