np = 0
n = 1

s = 0

while n < 4000000:
	current = n

	if (current % 2 == 0) :
		s = s + current

	n = current + np
	np = current

print(s)