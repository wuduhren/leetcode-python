def radixSort(nums):
    maxNumberOfDigits = len(str(max(nums)))
    
    for d in xrange(maxNumberOfDigits):
        b = [[] for _ in xrange(10)]

        for num in nums:
            n = (num//10**d)%10
            print num, d, n
            b[n].append(num)
        
        i = 0
        for a in b:
            for num in a:
                nums[i] = num
                i += 1


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
radixSort(test)
print test