def heapSort(A):
	#build max heap
	def heapify(A, n, i):
		if i>=n: return
		l, r = i*2+1, i*2+2
		left = A[l] if l<n else float('-inf')
		right = A[r] if r<n else float('-inf')

		if left>A[i] or right>A[i]:
			if left>right:
				A[i], A[l] = A[l], A[i]
				heapify(A, n, l)
			else:
				A[i], A[r] = A[r], A[i]
				heapify(A, n, r)

	n = len(A)

	for i in reversed(xrange(n)):
		heapify(A, n, i)

	for i in reversed(xrange(1, n)):
		A[i], A[0] = A[0], A[i]
		heapify(A, i, 0)



A = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
heapSort(A)
print A

"""
Time Complexity O(NLogN) in best, average, worst case.
Space Complexity O(1)
"""