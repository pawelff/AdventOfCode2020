f = open("day_5.txt").read().split('\n')

res = 0
seats = []
for line in f:
	row, col = 0, 0
	for i, c in enumerate(line):
		if c == 'B':
			row += 1<<(6-i)
		if c == 'R':
			col += 1<<(2+7-i)
			
	seats.append(row*8+col)
	res = max(res, (row*8+col))
	
print(f'Part one: {res}')

prev = 0
i = 0
seats.sort()
for seat in seats:
	if seat-2 == prev:
		print(f'Part one: {prev+1}')
		break
	prev = seat

