import itertools, operator

lines = open("input.txt", "r").read().split("\n")

def parse_line(line):
	words = line.split("-")
	name = "".join(words[:-1])
	sector_id = int(words[-1:][0][0:3])
	checksum = words[-1:][0][4:4+5]
	valid = False
	
	freqs = []
	
	for i in range(26):
		c = chr(i+97)
		freq = (c, name.count(c))
		freqs.append(freq)
	
	#print "\n".join([str(f) for f in freqs if f[0] > 0])
	
	sfreqs = sorted(freqs, key=lambda a: a[1], reverse=True)
	# print sfreqs
	most_common = "".join([f[0] for f in sfreqs])[:5]
	
	if most_common == checksum:
		valid = True
	
	res = (name, sector_id, checksum, valid)
	
	# print name, most_common, checksum, valid, sector_id
	
	return res
	
def decrypt(name, rot):
	offset = rot % 26
	res = ""
	for c in name:
		oc = ord(c) + offset
		if oc > ord("z"): 
			oc -= 26
		res += chr(oc)
	return res	
		
num_of_valid_rooms = 0
sum_of_valid_rooms = 0
f = open("asd.txt", "w")
for line in lines:
	room = parse_line(line)
	if room[3] == True:
		sum_of_valid_rooms += room[1]
		num_of_valid_rooms += 1
		f.write(decrypt(room[0], room[1])+str(room[1])+"\n")

print sum_of_valid_rooms, num_of_valid_rooms
