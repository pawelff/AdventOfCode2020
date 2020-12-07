from functools import lru_cache


f = open("input.txt").read().split('\n')

rules = {}
for rule in f:
	bc = rule.split(' bags contain')
	r = bc[1].split()
	i = 1
	d = {}
	while i<len(r):
		d.update({r[i]+' '+r[i+1]: r[i-1]})
		i+=4
	rules.update({bc[0]: d})


@lru_cache(maxsize=600)
def check_for_shiny_gold(bag):
	for contain in rules[bag]:
		if 'shiny gold' in contain:
			return True
		elif 'other bags.' in contain:
			return False
		else:
			if check_for_shiny_gold(contain):
				return True


#Part one
res = set()
for bag, contain in rules.items():
	contain = contain.keys()
	if 'shiny gold' in contain:
		res.add(bag)
	elif 'other bags.' in contain:
		continue
	else:
		for c in contain:
			if check_for_shiny_gold(c):
				res.add(bag)


print(len(res))


def part_two(bag):
	t = 0
	for b, qty in rules[bag].items():
		if b == 'other bags.':
			t += 0
		else:
			qty = int(qty)
			t += qty + qty*part_two(b)
	return t

	
#Part two
print(part_two('shiny gold'))