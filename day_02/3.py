valid_passwords = 0
with open("3.txt", "r") as f:
	for line in f:
		words = line.split()
		qty = list(map(int, words[0].split('-')))
		letter = words[1][0]
		password = words [2]
		num_of_letters_in_password = password.count(letter)
		if num_of_letters_in_password>= qty[0] and num_of_letters_in_password<=qty[1]:
			valid_passwords += 1


print(valid_passwords)