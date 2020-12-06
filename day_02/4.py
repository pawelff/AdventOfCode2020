valid_passwords = 0
with open("3.txt", "r") as f:
	for line in f:
		words = line.split()
		positions = list(map(int, words[0].split('-')))
		letter = words[1][0]
		password = words [2]
		if (password[positions[0]-1] == letter) != (password[positions[1]-1] == letter):
			valid_passwords += 1


print(valid_passwords)