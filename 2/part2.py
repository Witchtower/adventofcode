lines = open("input.txt", "r").read().split("\n")

keys = "123456789ABCD"

keypad = """       
   1   
  234  
 56789 
  ABC  
   D   
       """.split("\n")

def get_val(pos):
	return keypad[pos[1]][pos[0]]

def move(pos, c):
	if c == "U":
		return (pos[0], pos[1]-1)
	if c == "D":
		return (pos[0], pos[1]+1)
	if c == "L":
		return (pos[0]-1, pos[1])
	if c == "R":
		return (pos[0]+1, pos[1])

pos = (1, 3)

for line in lines:
	for c in line:
		if get_val(move(pos,c)) in keys:
			pos = move(pos, c)
	print get_val(pos)