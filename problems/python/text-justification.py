"""
The description of this problem is unclear.
"Extra spaces between words should be distributed as evenly as possible." Should be "Extra spaces between words IN EACH LINE should be distributed as evenly as possible."
So the problem in short is:
1. Every line should have as many as word as possible. But they should be separate by space or spaces.
2. Mid align all the line. Except the last line and the lines with one word.
3. For mid align, distribute space evenly, if there are extra spaces, it should be located left. For example 5 spaces distribute to 2 places, it should be 3 2, not 2 3. 7 spaces distribute to 3 places, it should be 3 2 2, not 2 3 2, not 2 2 3.

Time: O(N), N is the number of words.
Space: O(W), W is maxWidth for keeping strings in currLine. Can further reduce to O(1) using only index.
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        def canAddToCurrLine(word, currLineStringLength):
            currWidth = len(currLine)-1 + currLineStringLength # space+currLineStringLength
            return currWidth+len(word)+1<=maxWidth
        
        def leftAlign(currLine):
            line = ''
            
            for word in currLine:
                line += word + ' '
            line = line[:-1] #remove last space
            
            line += ' '*(maxWidth-len(line))
            return line
        
        def midAlign(currLine, currLineStringLength):
            line = ''
            
            totalSpaceCount = maxWidth-currLineStringLength
            extraSpaceCount = totalSpaceCount%(len(currLine)-1)
            spaceCount = totalSpaceCount-extraSpaceCount
            spaces = ' '*(totalSpaceCount/(len(currLine)-1))
            
            for word in currLine:
                line += word
                if spaceCount>0:
                    line += spaces
                    spaceCount -= len(spaces)
                
                if extraSpaceCount>0:
                    line += ' '
                    extraSpaceCount -= 1
                    
            return line
            
        currLineStringLength = 0
        currLine = []
        ans = []
        
        i = 0
        while i<len(words):
            if canAddToCurrLine(words[i], currLineStringLength):
                currLine.append(words[i])
                currLineStringLength += len(words[i])
                i += 1
            else:
                if len(currLine)==1:
                    ans.append(leftAlign(currLine)) #line with one word align left
                else:
                    ans.append(midAlign(currLine, currLineStringLength))
                
                currLine = []
                currLineStringLength = 0
                
        ans.append(leftAlign(currLine)) #last line should always align left
        return ans