import math


data = open("input.txt").read().splitlines()
data = list(map(int, data))
data.sort(reverse=True)

diff_3 = 1
diff_1 = 1
for i in range(0, len(data)-1):
	diff = data[i] - data[i+1]
	if diff == 3: diff_3 += 1
	elif diff == 1:  diff_1 += 1

	
#Part one
print(f' Part one: {diff_3 * diff_1}')


s = set(data)
diffs = []
for i in range(0, len(data)-1):
	a = range(data[i]-3, data[i])
	diffs.append(len(s.intersection(set(a))))

print(math.prod(diffs)-1)
