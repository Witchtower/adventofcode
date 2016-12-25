import operator
#get the input
way = [(i[:1], int(i[1:])) for i in map(str.strip, open("input.txt", "r").read().split(","))]

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)] # n w s o
cdir = 0 # initial direction is north
pos = (0, 0) # start at (0, 0) cuz everything is relative
visited = [pos] # save places we've been in a list

for newdir, distance in way:
	# turn
	if newdir == "L": cdir -= 1
	else: cdir += 1
	cdir = cdir % 4 # yes, that also makes a -1 to a 3
	# move
	for i in range(distance):
		pos = tuple(map(operator.add, pos, dirs[cdir])) # go one step
		if pos in visited: # were we already here?
			# this is the end of the program
			print sum(map(abs, pos))
			exit()
		visited.append(pos) # remember that place
		
	