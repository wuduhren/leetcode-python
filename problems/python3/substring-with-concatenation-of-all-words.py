"""
Time: O(W * N/W * W), there will be W time of iteration in the first loop ([0]), N/W of iteration in the second loop ([1]). In each loop, creating substring "word" and "popWord" takes O(W).
Space: O(MW) for "wordSet".
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(s)
        M = len(words)
        W = len(words[0])
        wordSet = set(words)
        ans = []
        counter = collections.Counter(words)
        
        for i in range(W): #[0]
            windowCounter = collections.Counter() #counter for the word in words
            notInWords = 0 #number of word not in the wordSet
            theSame = 0 #number of word with the same count with "counter"
            j = i
            
            while j<N: #[1]
                word = s[j:j+W]
                if word in wordSet:
                    windowCounter[word] += 1
                    if windowCounter[word]==counter[word]:
                        theSame += 1
                    elif windowCounter[word]>counter[word]:
                        theSame -= 1
                else:
                    notInWords += 1
                    
                popStart = j-M*W
                if popStart>=0:
                    popWord = s[popStart:popStart+W]
                    if popWord in wordSet:
                        windowCounter[popWord] -= 1
                        if windowCounter[popWord]==counter[popWord]:
                            theSame += 1
                        elif windowCounter[popWord]<counter[popWord]:
                            theSame -= 1
                    else:
                        notInWords -= 1
                
                if theSame==len(wordSet) and notInWords==0: ans.append(popStart+W)
                j += W
                
        return ans