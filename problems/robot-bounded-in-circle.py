class Solution(object):
    def isRobotBounded(self, instructions):
        direction = 0
        x = y = 0
        
        for i in instructions:
            if i=='L':
                direction -= 1
                direction = direction%4
            elif i=='R':
                direction += 1
                direction = direction%4
            elif i=='G':
                if direction==0:
                    y+=1
                elif direction==1:
                    x+=1
                elif direction==2:
                    y-=1
                elif direction==3:
                    x-=1
        
        moved = (x, y) != (0, 0)
        rotated = direction!=0

        if not moved: return True
        if moved and rotated: return True
        if moved and not rotated: return False