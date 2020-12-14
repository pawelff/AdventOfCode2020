from time import time
data = open("input.txt").read().splitlines()

st = time()
#part one
mask = 0
values = {}
for line in data:
	line = line.split(' = ')
	if line[0] == 'mask':
		mask = line[1]
	else:
		idx = line[0][4:-1]
		value = list(reversed(bin(int(line[1]))))[:-2]
		value = value + ['0']*(36 - len(value))
		for i, bit in enumerate(reversed(mask)):
			if bit == 'X':
				continue
			else:
				value[i] = bit
		values[idx] = int(''.join(reversed(value)),2)
	

res = 0
for val in values.values():
	res += val

print(time()-st)
print(f'Part one: {res}')