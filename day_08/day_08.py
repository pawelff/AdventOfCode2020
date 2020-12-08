import copy


data = open("input.txt").read().split('\n')
instructions = []
for line in data:
	splited = line.split()
	instructions.append({'instr': splited[0], 'arg': int(splited[1]), 'exec': 0})


def is_infinite_loop(instructions):
	i = 0
	acc = 0
	while True:
		instructions[i]['exec'] += 1
		if instructions[i]['exec'] == 2:
			return True, acc
		if instructions[i]['instr'] == 'nop': i += 1
		elif instructions[i]['instr'] == 'acc':
			acc += instructions[i]['arg']
			i += 1
		else: i += instructions[i]['arg']
		if i == 652:
			return False, acc
			
		
#part one
_, acc = is_infinite_loop(copy.deepcopy(instructions))
print(acc)


#part two
for j, instr in enumerate(instructions):
	instr_copy = copy.deepcopy(instructions)
	if instr_copy[j]['instr'] == 'nop':
		instr_copy[j]['instr'] = 'jmp'
	elif instr_copy[j]['instr'] == 'jmp':
		instr_copy[j]['instr'] = 'nop'
	else:
		continue
	inf, acc = is_infinite_loop(instr_copy)
	if not inf:
		print(acc)
		break
