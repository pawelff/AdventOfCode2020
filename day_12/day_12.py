from copy import deepcopy


data = open("input.txt").read().splitlines()


#part one
positions = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
directions = ['E', 'S', 'W', 'N']
direction = 0 #^ initial direction is east
for instr in data:
	action, value = instr[0], int(instr[1:])
	if action == 'R':
		direction += value//90
		direction %= 4
	elif action == 'L':
		direction -= value//90
		direction %= 4
	elif action in 'NESW':
		positions[action] += value
	else: #action F
		positions[directions[direction]] += value


result = abs(positions['N'] - positions['S']) + abs(positions['E'] - positions['W'])

print(f'Part one: {result}')


#part two
positions = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
directions = ['E', 'S', 'W', 'N']
direction = 0
waypiont = {'N': 1, 'E': 10, 'S': 0, 'W': 0}
for instr in data:
	action, value = instr[0], int(instr[1:])
	if action == 'F':
		for wp, val in waypiont.items():
			positions[wp] += val*value
	elif action in 'NESW':
		waypiont[action] += value
	else:
		direction = value//90
		if action == 'L':
			direction *= -1
		rotateds = []
		for d, v in deepcopy(waypiont).items():
			if v == 0:
				continue
			else:
				rotated = directions[(directions.index(d) + direction) % 4]
				waypiont[rotated] = v
				rotateds.append(rotated)
		for wp in set(directions)-set(rotateds):
			waypiont[wp] = 0
			


result = abs(positions['N'] - positions['S']) + abs(positions['E'] - positions['W'])
print(f'Part two: {result}')