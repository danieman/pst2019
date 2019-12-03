from string import ascii_lowercase, ascii_uppercase


def transpose(char, key):
	if char.isupper():
		alph = ascii_uppercase + 'ÆØÅ'
	elif char.islower():
		alph = ascii_lowercase + 'æøå'
	else:
		return char
	return alph[(alph.index(char) + key) % len(alph)]


def print_flag(candidates):
	for s in candidates:
		if 'PST' in s:
			print('\nSolution is probably:')
			s = s.replace(' krøllparantes slutt', '}')
			s = s.replace(' krøllparantes ', '{')
			print(s)
			print()


cipher = 'KNO fmwggkymyioån 30å6ø8432æå54710a9æ09a305å7z9829 fmwggkymyioån ngpoo'
candidates = []

# Brute force key:
for key in range(29):	
	plain = ''
	for c in cipher:
		plain += transpose(c, key)
	candidates.append(plain)
	print(f'Key {str(key).zfill(2)}: {plain}')

# Print probable solution
print_flag(candidates)