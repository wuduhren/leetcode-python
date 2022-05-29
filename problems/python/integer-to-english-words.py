class Solution(object):
    def numberToWords(self, num):
        underTwenty = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', ]
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        
        def toWords(n):
            if n==0:
                return []
            elif n<20:
                return [underTwenty[n]]
            elif n<100:
                c, r = n/10, n%10
                return [tens[c]] + toWords(r)
            elif n<1000:
                c, r = n/100, n%100
                return toWords(c) + ['Hundred'] + toWords(r)
            else:
                if n>=1000000000:
                    c, r = n/1000000000, n%1000000000
                    return toWords(c) + ['Billion'] + toWords(r)
                elif n>=1000000:
                    c, r = n/1000000, n%1000000
                    return toWords(c) + ['Million'] + toWords(r)
                elif n>=1000:
                    c, r = n/1000, n%1000
                    return toWords(c) + ['Thousand'] + toWords(r)

        return ' '.join(toWords(num)) or 'Zero'