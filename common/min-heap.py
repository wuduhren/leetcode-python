class MinHeap(object):
	def __init__(self):
		self.heap = []
		self.size = 0

	def push(self, x):
		def bubbleUp(i):
			p = max((i-1)//2, 0)
			if self.heap[p]>self.heap[i]:
				self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
				bubbleUp(p)

		self.heap.append(x)
		bubbleUp(self.size)
		self.size += 1

	def pop():
		if self.size<=0: return None
		m = self.heap[0]
		remove(0)
		return m

	def remove(self, i):
		def bubbleDown(i):
			l = i*2+1
			r = i*2+2
			left_child = self.heap[l] if l<self.size else float('inf')
			right_child = self.heap[r] if r<self.size else float('inf')

			if self.heap[i]>left_child or self.heap[i]>right_child:
				if left_child<right_child:
					self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
					bubbleDown(l)
				else:
					self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
					bubbleDown(r)

		if i>=self.size:
			return
		elif i==self.size-1:
			self.heap = self.heap[:-1]
			self.size -= 1
			return
		else:
			self.heap[i], self.heap[-1] = self.heap[-1], self.heap[i]
			self.heap = self.heap[:-1]
			self.size -= 1
			bubbleDown(i)
			return






min_heap = MinHeap()
min_heap.push(3)
min_heap.push(1)
min_heap.push(2)
min_heap.push(10)
min_heap.push(4)
min_heap.push(7)
min_heap.push(9)

print min_heap.heap

min_heap.remove(2)
print min_heap.heap

min_heap.remove(2)
min_heap.remove(2)
min_heap.remove(2)
min_heap.remove(2)
print min_heap.heap

min_heap.remove(2)
min_heap.remove(1)
min_heap.remove(0)
print min_heap.heap

		