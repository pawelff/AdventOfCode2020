data = open("input.txt").read().splitlines()
from pprint import pprint


def make_round(data, p2=False):
	new_layout = []
	for ri, row in enumerate(data):
		new_row = []
		for si, seat in enumerate(row):
			if seat == '.':
				new_row.append('.')
				continue
			occ = 0
			change = -1
			while si+change >= 0:
				if row[si+change] == '#':
					occ += 1
					break
				elif p2 and row[si+change] == '.':
					change += -1
				elif p2 and row[si+change] == 'L':
					break
				if not p2: break
			change = 1
			while si+change < len(row):
				if row[si+change] == '#':
					occ += 1
					break
				elif p2 and row[si+change] == '.':
					change += 1
				elif p2 and row[si+change] == 'L':
					break
				if not p2: break
			change = -1
			diag1, up, diag2 = False, False, False
			while ri+change >= 0:
				if not diag1 and si+change >= 0:
					if data[ri+change][si+change] == '#':
						occ += 1
						diag1 = True
					elif data[ri+change][si+change] == 'L':
						diag1 = True
				if not up:
					if data[ri+change][si] == '#':
						occ += 1
						up = True
					elif data[ri+change][si] == 'L':
						up = True
				if not diag2 and si < len(row)+change:
					if data[ri+change][si-change] == '#':
						occ += 1
						diag2 = True
					elif data[ri+change][si-change] == 'L':
						diag2 = True
				if not p2: break
				if not all([diag1, up, diag2]):
					change += -1
				else: break
			change = 1
			diag1, down, diag2 = False, False, False
			while ri+change < len(data):
				if not diag1 and si+change < len(row):
					if data[ri+change][si+change] == '#':
						occ += 1
						diag1 = True
					elif data[ri+change][si+change] == 'L':
						diag1 = True
				if not down:
					if data[ri+change][si] == '#':
						occ += 1
						down = True
					elif data[ri+change][si] == 'L':
						down = True
				if not diag2 and si-change >= 0:
					if data[ri+change][si-change] == '#':
						occ += 1
						diag2 = True
					elif data[ri+change][si-change] == 'L':
						diag2 = True
				if not p2: break
				if not all([diag1, down, diag2]):
					change += 1
				else: break
			if seat == 'L' and occ == 0:
				new_row.append('#')
			elif seat == '#' and occ >= (4 if not p2 else 5):
				new_row.append('L')
			else:
				new_row.append(seat)
		new_layout.append(''.join(new_row))
	if data != new_layout:
		return make_round(new_layout, p2)
	else:
		occ = 0
		for row in new_layout:
			occ += row.count('#')
		return occ
	
	
print(f'Part one: {make_round(data)}')
print(f'Part two: {make_round(data, True)}')