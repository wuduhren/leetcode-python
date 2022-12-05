"""
Original's solution
Time: O(MN)
Space: O(1)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        x0 = 0
        y0 = 0
        dx = len(matrix[0])-1
        dy = len(matrix)-1
        direction = 'right'
        isFirst = True
        
        ans.append(matrix[x0][y0])
        while True:
            if direction=='right':
                for x in range(x0+1, x0+dx+1):
                    ans.append(matrix[y0][x])
                x0 += dx
                direction = 'down'
                
                if isFirst:
                    isFirst = False
                else:
                    dx -= 1
                
                if dy==0: break
            
            elif direction=='left':
                for x in range(x0-1, x0-dx-1, -1):
                    ans.append(matrix[y0][x])
                x0 -= dx
                direction = 'up'
                dx -= 1
                if dy==0: break
            
            elif direction=='down':
                for y in range(y0+1, y0+dy+1):
                    ans.append(matrix[y][x0])
                y0 += dy
                direction = 'left'
                dy -= 1
                if dx==0: break
            
            elif direction=='up':
                for y in range(y0-1, y0-dy-1, -1):
                    ans.append(matrix[y][x0])
                y0 -= dy
                direction = 'right'
                dy -= 1
                if dx==0: break
        return ans


"""
Answer from Neetcode, more elegant.
left, right, top, bottom is the border (index is exclusive on the border.
In other words, for matrix[i][j]
i: top<i<bottom
j: left<j<right
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res