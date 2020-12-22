#solution I saw on Internet
import re


data = open("input.txt").read().splitlines()

class p1(int):
	def __add__(self, other):
		return p1(int(self) + int(other))
	
	def __sub__(self, other):
		return p1(int(self) * int(other))

		
class p2(int):
	def __mul__(self, other):
		return p2(int(self) + int(other))
	
	def __sub__(self, other):
		return p2(int(self) * int(other))

res = 0
for line in data:
	line = line.replace('*', '-')
	line = re.sub('(\d+)', r'p1(\1)', line)
	res += eval(line)

print(f'Part one: {res}')	


res = 0
for line in data:
	line = line.replace('*', '-').replace('+', '*')
	line = re.sub('(\d+)', r'p2(\1)', line)
	res += eval(line)
	
print(f'Part two: {res}')
