from time import time
from collections import deque


data = open("input.txt").read().splitlines()


st = time()

d1, d2 = deque(), deque()
p2 = False
for line in data[1:]:
	if line == '': continue
	if line == 'Player 2:':
		p2 = True
		continue
	if p2:
		d2.append(int(line))
		continue
	d1.append(int(line))

	
def play(d1, d2):
	while d1 and d2:
		p1 = d1.popleft()
		p2 = d2.popleft()
		if p1 > p2:
			d1.append(p1)
			d1.append(p2)
		else:
			d2.append(p2)
			d2.append(p1)
	return d1 if len(d2) == 0 else d2 
	

win = play(d1, d2)
win.reverse()
res = 0

for i, card in enumerate(win):
	res += card * (i+1)


print(f'Part one: {res}')
print(f'Part one time: {time()-st}')
