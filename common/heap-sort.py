#O(LogN), used when part of the array is already heapified.
def heapify(A, N, i):
	largest = i
	l = i*2+1
	r = i*2+2

	if l<N and A[l]>A[largest]: largest = l
	if r<N and A[r]>A[largest]: largest = r
	if largest!=i:
		A[largest], A[i] = A[i], A[largest]
		heapify(A, N, largest)

#O(NLogN)
def heapSort(A):
	N = len(A)

	#build max heap, O(NLogN). Can be optimized to the O(N).
	for i in range(N//2-1, -1, -1):
		heapify(A, N, i)
	
	#keep swapping the largest
	for i in range(N-1, -1, -1):
		A[0], A[i] = A[i], A[0]
		heapify(A, i, 0)


A = [12, 11, 13, 5, 6, 7]
heapSort(A)
print(A)

A = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
heapSort(A)
print(A)