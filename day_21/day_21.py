from time import time
from collections import defaultdict


data = open("input.txt").read().splitlines()


st = time()
algd = defaultdict(list)
for line in data:
	ing, alg = line.split(' (contains ')
	algs = alg[:-1].split(', ')
	ing = ing.split()
	for alg in algs:
		algd[alg].append(ing)
		

algs = set()
for alg, ings in algd.items():
	s = set(ings[0])
	for ing in ings[1:]:
		s = s.intersection(set(ing))
	algd[alg] = list(s)
	algs = algs.union(s)
	
	
res = 0
for line in data:
	ing, _ = line.split(' (contains ')
	ing = set(ing.split())
	res += len(ing.difference(algs))
	

print(f'Part one: {res}')
print(f'Part one time: {time()-st}')
