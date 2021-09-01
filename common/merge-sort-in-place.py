def merge(A, start, mid, end):
    L, R = A[start:mid], A[mid:end]
    i = j = 0
    k = start
    for l in xrange(k,end):
        if j>=len(R) or (i<len(L) and L[i]<R[j]):
            A[l] = L[i]
            i = i+1
        else:
            A[l] = R[j]
            j = j+1

def mergeSort(A, p, r):
    if r - p > 1:
        mid = (p+r)/2
        mergeSort(A, p, mid)
        mergeSort(A, mid, r)
        merge(A, p, mid, r)

A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
mergeSort(A, 0, len(A))
print A
