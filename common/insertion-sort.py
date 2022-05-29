def insertionSort(nums):
	for i in xrange(len(nums)):
		num = nums[i]
		j = i-1
		while j>=0 and num<nums[j]:
			nums[j+1] = nums[j]
			j-=1
		nums[j+1] = num
	return nums


if __name__ == '__main__':
	test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
	print insertionSort(test)

"""
Time Complexity is O(N^2) in average and worst case. O(N) in best case.
Space Complexity is O(1).
"""