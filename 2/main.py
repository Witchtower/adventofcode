lines = open("input.txt", "r").read().split("\n")

pos = 5

for line in lines:
	for c in line:
		if c == "U" and pos > 3:
			pos -= 3
		elif c == "D" and pos < 7:
			pos += 3
		elif c == "L" and pos not in [1,4,7]:
			pos -= 1
		elif c == "R" and pos not in [3,6,9]:
			pos += 1
	print pos, chr(pos)