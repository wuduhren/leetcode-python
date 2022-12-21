class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        needAdditionDigit = True

        while i>=0 and needAdditionDigit:
            if digits[i]==9:
                digits[i] = 0
                i -= 1
                needAdditionDigit = True
            else:
                digits[i] += 1
                needAdditionDigit = False
        if needAdditionDigit: digits.insert(0, 1)
        return digits
        