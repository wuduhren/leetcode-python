class Solution(object):
    def groupStrings(self, strings):
        def getHash(string):
            h = ''
            offset = getNumByChar(string[0])*-1
            for c in string:
                h += getCharByNum((getNumByChar(c)+offset) if (getNumByChar(c)+offset)>=0 else 26+(getNumByChar(c)+offset))
            return h
        
        def getNumByChar(letter):
            return ord(letter) - 97

        def getCharByNum(pos):
            return chr(pos + 97)
        
        groups = collections.defaultdict(list)
        for string in strings:
            h = getHash(string)
            groups[h].append(string)
        return groups.values()