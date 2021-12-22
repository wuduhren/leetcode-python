class Solution(object):
    def spiralOrder(self, matrix):
        ans = []
        i, j = 0, 0
        direction = 'right'
        count = 0
        
        while count<=len(matrix)*len(matrix[0]):
            iNext, jNext = i, j
            
            if direction=='right':
                if j+1<len(matrix[0]) and matrix[i][j+1]!='v':
                    jNext = j+1
                else:
                    direction = 'down'
            elif direction=='down':
                if i+1<len(matrix) and matrix[i+1][j]!='v':
                    iNext = i+1
                else:
                    direction = 'left'
            elif direction=='left':
                if j-1>=0 and matrix[i][j-1]!='v':
                    jNext = j-1
                else:
                    direction = 'up'
            elif direction=='up':
                if i-1>=0 and matrix[i-1][j]!='v':
                    iNext = i-1
                else:
                    direction = 'right'
            
            if (iNext, jNext)!=(i, j) or count>=len(matrix)*len(matrix[0])-1:
                ans.append(matrix[i][j])
                matrix[i][j] = 'v' #visited
                count += 1
                i = iNext
                j = jNext

        return ans[:-1]
                
        
        