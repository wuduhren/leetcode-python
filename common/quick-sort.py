def quickSort(A):
	def sortRange(A, l, r):
		if l>=r: return A

		p = A[(l+r)/2]
		i = partition(A, l, r, p)
		sortRange(A, l, i-1)
		sortRange(A, i, r)
		return A

	def partition(A, l, r, p):
		while l<=r:
			while A[l]<p: l += 1
			while A[r]>p: r -= 1
			if l<=r:
				A[l], A[r] = A[r], A[l]
				l += 1
				r -= 1
		return l

	return sortRange(A, 0, len(A)-1)


A = [5,2,4,1,3,6,0]
print quickSort(A)


"""
Time Complexity is O(NlogN) on best and average case.
O(N^2) on the worst case, because if you choose the smallest pivot everytime the array will decay in a linear time.
Space Complexity O(LogN), for we need to store the stack for the recursion.
"""