import Queue

class PriorityQueue(Queue.Queue):
	def _init(self,maxSize):
		self.queue = []
	def _qsize(self, len=len):
		return len(self.queue)
	def put_l2h(self, item):
		data,priority = item
		self._insort_right((priority, data))
	def put_h2l(self, item):
		data,priority = item
		self._insort_left((priority, data))
	def remove(self, instID):
		for i in range(qsize()):
			if(i is instID):
				return true
		return false
		
		
	def _get(self):
		return self.queue.pop(0)[1]
	def _insort_right(self, x):
		"""Insert item x in list, and keep it sorted from low to high assuming a is sorted.
		If x is already in list, insert it to the right of the rightmost x.       
		"""
		a = self.queue
		lo = 0        
		hi = len(a)

		while lo < hi:
			mid = (lo+hi)/2
			if x[0] < a[mid][0]: hi = mid
			else: lo = mid+1
		a.insert(lo, x)
	def _insort_left(self, x):
		"""Insert item x in list, and keep it sorted from high to low assuming a is sorted.
		If x is already in list, insert it to the right of the rightmost x.       
		"""
		a = self.queue
		lo = 0        
		hi = len(a)

		while lo < hi:
			mid = (lo+hi)/2
			if x[0] > a[mid][0]: hi = mid
			else: lo = mid+1
		a.insert(lo, x)
def test():
	pq = PriorityQueue()

	pq.put_h2l(('b', 1.23))
	pq.put_h2l(('a', 1))
	pq.put_h2l(('c', 1))
	pq.put_h2l(('z', 0))
	pq.put_h2l(('d', 2))
	print(pq.qsize())
	while not pq.empty():
		print(pq.get())

#test() 