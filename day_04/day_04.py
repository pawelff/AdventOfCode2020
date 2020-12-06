import re

f = open("day_4.txt").read().replace('\n', ' '). split('  ')
s = set()
required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
fields = {
	'byr': lambda byr: 1920 <= int(byr) <= 2002,
	'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
	'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
	'hgt': lambda hgt: 150 <= int(hgt[:-2]) <= 193 if hgt[-2:]== 'cm' else  59 <= int(hgt[:-2]) <= 76 if hgt[-2:] == 'in' else False,
	'hcl': lambda hcl: re.match(r'^#[0-9a-f]{6}$', hcl),
	'ecl': lambda ecl: ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
	'pid': lambda pid: pid.isnumeric() and len(pid) == 9,
	'cid': lambda c: True
}


valid = 0
valid2 = 0
for line in f:
	for pair in line.split():
		s.add(pair.split(':')[0])
	if required <= s:
		valid += 1
		for pair in line.split():
			k, v = pair.split(':')
			if not fields[k](v):
				break
		else:
			valid2 += 1
	s.clear()
	
print(valid)
print(valid2)
