import itertools, operator

lines = open("input.txt", "r").read().split("\n")
numlists = [[],[],[]]
for line in lines:
	nums = [int(line[i:i+5]) for i in range(0,15,5)]
	for i in range(3):
		numlists[i].append(nums[i])
		
allnums = []
map(allnums.extend, numlists)
	
possible_triangles = 0

for i in range(0, len(allnums), 3):
	nums = allnums[i:i+3]
	valid = True
	#0 
	if nums[0] >= nums[1] + nums[2]:
		valid = False
	#1
	if nums[1] >= nums[0] + nums[2]:
		valid = False
	#2
	if nums[2] >= nums[0] + nums[1]:
		valid = False
	
	if valid:
		possible_triangles += 1

print possible_triangles