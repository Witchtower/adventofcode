lines = map(list, open("input.txt", "r").read().split("\n"))

columns = [[] for i in range(len(lines[0]))]

res = []

for line in lines:
	for i in range(len(line)):
		columns[i].append(line[i])
		
for column in columns:
	occurrance = []
	for i in range(ord("a"), ord("z")+1):
		occurrance.append((chr(i), column.count(chr(i))))
	top = sorted(occurrance, key=lambda x: x[1])[::-1][0]
	res.append(top)
	
print "".join([res[i][0] for i in range(len(res))])