class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0': return '0'
        M, N = len(num1), len(num2)
        temp = [0]*(M+N+1)

        num1, num2 = num1[::-1], num2[::-1]
        for i in range(M):
            for j in range(N):
                digits = int(num1[i])*int(num2[j])
                temp[i+j] += digits
                temp[i+j+1] += temp[i+j]//10
                temp[i+j] = temp[i+j]%10
        
        ans = ''
        temp = temp[::-1]
        isLeadingZero = True
        for d in temp:
            if d!=0 or not isLeadingZero:
                isLeadingZero = False
                ans += str(d)
        return ans