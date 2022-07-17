class Codec:
    def encode(self, strs: List[str]) -> str:
        output = ''
        for string in strs:
            output += str(len(string))+'#'+string
        return output
        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        
        while i<len(s):
            j = i+1
            
            while s[j]!='#': j += 1
                    
            l = int(s[i:j])
            string = s[j+1:j+1+l]
            output.append(string)
            i = j+1+l
            
        return output