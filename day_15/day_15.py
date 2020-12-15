input = '7,12,1,0,16,2'
input = list(map(int, input.split(',')))


def solve_part(part):
	loop = 30000001 if part == 2 else 2021
	turn = 1
	last_spoken = {}
	last = 0
	for num in input:
		last_spoken[num] = (0, turn)
		last = num
		turn += 1
		

	while turn != loop:
		if last_spoken[last][0] == 0:
			last = 0
			sd = last_spoken.setdefault(last, (0, turn))
			if sd != (0, turn):
				last_spoken[last] = (sd[1], turn)
		else:
			last = last_spoken[last][1] - last_spoken[last][0]
			sd = last_spoken.setdefault(last, (0, turn))
			if sd != (0, turn):
				last_spoken[last] = (sd[1], turn)
		turn += 1
	return last
	
	
print(f'Part one: {solve_part(1)}')
print(f'Part two: {solve_part(2)}')