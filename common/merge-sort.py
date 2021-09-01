def mergeSort(A):
	def merge(a1, a2):
		opt = []
		i1 = i2 = 0
		while i1<len(a1) and i2<len(a2):
			if a1[i1]<a2[i2]:
				opt.append(a1[i1])
				i1+=1
			else:
				opt.append(a2[i2])
				i2+=1
		if i1<len(a1): opt.extend(a1[i1:])
		if i2<len(a2): opt.extend(a2[i2:])
		return opt

	m = len(A)/2
	if A is None or len(A)<=1: return A
	return merge(mergeSort(A[:m]), mergeSort(A[m:]))

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print mergeSort(test)

"""
Time Complexity is O(NLogN) for every cases.
Merging in every level takes O(N).
There are logN level.

Space Complexity is O(N)
"""





























