def get_max_value(value, weight, max_weight):
	N = len(value)
	K = [[0 for _ in xrange(max_weight+1)] for _ in xrange(N+1)]
	bag = []

	for i in xrange(N+1):
		for mw in xrange(max_weight+1):
			if i==0 or mw==0:
				K[i][mw] = 0
				continue
			w = weight[i-1]
			v = value[i-1]
			if w>mw:
				K[i][mw] = K[i-1][mw]
			else:
				K[i][mw] = max(v+K[i-1][mw-w], K[i-1][mw])

	max_value = K[-1][-1]

	w = max_weight
	i = N
	while i>0:
		if K[i][w]-K[i-1][w]>0:
			bag.append(i-1)
			w = w - weight[i-1]
		i = i-1

	print 'bag: ', bag
	print 'max_value', max_value
	return max_value


value = [60, 100, 120]
weight = [10, 20, 30]
max_weight = 50
get_max_value(value, weight, max_weight)

value = [40, 100, 50, 60]
weight = [20, 10, 40, 30]
max_weight = 60
get_max_value(value, weight, max_weight)

