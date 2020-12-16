from time import time
data = open("input.txt").read().split('\n\n')

s=time()
rules = {}
one_big_rule = set()
for line in data[0].split('\n'):
	rule, ranges = line.split(':')
	ranges = ranges.split(' or ')
	rules[rule] = []
	for r in ranges:
		low, high = r.split('-')
		r = range(int(low), int(high)+1)
		rules[rule] += list(r)
		one_big_rule |= set(r)

		
res = 0
valid_tickets = []
for nt in data[2].split('\n')[1:]:
	values = [int(x) for x in nt.split(',')]
	for v in values:
		if v not in one_big_rule:
			res += v
			break
	else:
		valid_tickets.append(values)	
	

print(f'Part one: {res}')
print(f'Part one: {time()-s}')


my_ticket = [int(x) for x in data[1].split('\n')[1].split(',')]
order = {}


for idx, num in enumerate(my_ticket):
	valid_rules = set()
	for rule, range in rules.items():
		if num in range:
			valid_rules.add(rule)
	order.update({idx: valid_rules})


for ticket in valid_tickets:
	for idx, num in enumerate(ticket):
		valid_rules = set()
		for rule, range in rules.items():
			if num in range:
				valid_rules.add(rule)
		order[idx] = order[idx].intersection(valid_rules)


len_one = 0
while True:
	for o, v in order.items():
		if len(v) == 1:
			len_one += 1
			for ord in order:
				if len(order[ord]) == 1:
					continue
				order[ord] = order[ord].difference(v)

	if len_one == len(order):
		break
	len_one = 0	


res = 1
for o, v in order.items():
	if v.pop().startswith('departure'):
		res *= my_ticket[o]
		
		
print(f'Part two: {res}')
print(f'Two parts time: {time()-s}')