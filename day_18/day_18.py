from time import time
data = open("input.txt").read().splitlines()

s=time()

def evaluate_parantheses(expr):
	res = int(expr[0])
	for i in range(1, len(expr)-1, 2):
		print(expr[i], expr[i+1])
		if expr[i] == '+':
			res += int(expr[i+1])
		else:
			res *= int(expr[i+1])
	print(f'Paranthestes: {res}')
	return res
	
	
def eval_expr(expr):
	while '(' in expr:
		for i in range(0, len(expr)-1, 2):
			if '(' not in expr[i:i+3]:
				r = evaluate_parantheses(expr[i:i+3])
				expr = [str(r)] + expr[i+3:]
				break
			else:
				
	return evaluate_parantheses(expr)		
	
	
for expr in data:
	expr = expr.split()
	eval_expr(expr)
print(f'Part one: {time()-s}')
