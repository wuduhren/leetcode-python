class Solution(object):
    def restoreIpAddresses(self, s):
        def search(digit, ip):
            if len(ip)==4:
                if len(digit)==0: opt.append(ip)
                return

            for i in xrange(1, len(digit)+1):
                num = int(digit[:i])
                if 0<=num and num<=255 and len(digit[:i])==len(str(num)):
                    search(digit[i:], ip+[digit[:i]])
        opt = []
        search(s, [])
        return ['.'.join(ip) for ip in opt]
