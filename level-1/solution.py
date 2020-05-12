def solution(data, n):
	t = {}
	for d in data:
		t[d] = t.get(d, 0) + 1
	for d in t:
		if t[d] > n:
			for i in range(t[d]):
				data.remove(d)
	return data