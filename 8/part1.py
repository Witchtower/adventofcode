commands = open("input.txt", "r").read().split("\n")

screen = []
for i in range(6):
	screen.append([0 for i in range(50)])

def rect(x,y):
	for iy in range(y):
		for ix in range(x):
			screen[iy][ix] = 1
	
def shift_row(i):
		row = screen[i]
		row = row[-1:] + row[:-1]
		screen[i] = row
		
def shift_col(i):
	item = screen[len(screen)-1][i]
	for j in range(len(screen)):
		tmp = screen[j][i]
		screen[j][i] = item
		item = tmp
		
def rotate(direction, rowcol, times):
	if direction == "row":
		for i in range(times):
			shift_row(rowcol)
	else:
		for i in range(times):
			shift_col(rowcol)
	
def display(scrn):
	res = []
	for row in scrn:
		s = ""
		for c in row:
			if c: s += "#"
			else: s += " "
		print s

for command in commands:
	words = command.split(" ")
	if words[0] == "rect":
		rect(*map(int,words[1].split("x")))
	elif words[0] == "rotate":
		rotate(words[1], int(words[2].split("=")[1]), int(words[4]))
display(screen)

summe = 0
for j in range(6):
	for i in range(50):
		summe += screen[j][i]


print summe
	