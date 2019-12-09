from string import ascii_lowercase, ascii_uppercase, digits


def transpose(char, key):
    if char.isupper():
        alph = ascii_uppercase + 'ÆØÅ'
    elif char.islower():
        alph = ascii_lowercase + 'æøå'
    elif char.isdigit():
        alph = digits
        return alph[(alph.index(char) - 4) % len(alph)]
    else:
        return char
    return alph[(alph.index(char) + key) % len(alph)]


def print_flag(s):
    if 'PST' in s:
        print('\nSolution is probably:')
        s = s.replace(' krø11p4r3n735 51u77', '}')
        s = s.replace(' krø11p4r3n735 ', '{')
        print(s)
        print()


cipher = 'KNO fmw55k8m7i179 z98øyåz8æy67aåy0å6æ7aø1å1438åa5a fmw55k8m7i179 95p11'
plain = ''

for c in cipher:
    plain += transpose(c, 5)

# Print probable solution
print_flag(plain)