#https://leetcode.com/problems/fizz-buzz/
class Solution(object):
    def fizzBuzz(self, n):
        nums = []
        for num in range(1, n+1):
            
            if num%3==0 and num%5==0:
                nums.append('FizzBuzz')
            elif num%3==0:
                nums.append('Fizz')
            elif num%5==0:
                nums.append('Buzz')
            else:
                nums.append(str(num))

        return nums