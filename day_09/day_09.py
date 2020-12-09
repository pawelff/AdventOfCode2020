data = open("input.txt").read().splitlines()
data = list(map(int, data))

def first_invalid_number_xmas(cipher, preamble):
	for i, num in enumerate(cipher[preamble:]):
		count = 0
		for prev_num in cipher[i:preamble+i]:
			if (num - prev_num) not in cipher[i:preamble+i] and (num - prev_num) != prev_num:
				count += 1
		if count == preamble:
			return num
				

invalid = first_invalid_number_xmas(data, 25)
print(f'Parto one: {invalid}')

def encryption_weakness(cipher, invalid):
	for i in range(2, len(cipher)):
		for j, num in enumerate(cipher):
			if sum(cipher[j:j+i]) == invalid:
				return min(cipher[j:j+i]) + max(cipher[j:j+i])
		
		
print(f'Part two: {encryption_weakness(data, invalid)}')