from hashlib import md5

input = "reyedfim"

index = 0

res = ""

while len(res) < 8:
	hash = md5(input+str(index)).hexdigest()
	#print hash, hash[:5]
	if hash[:5] == "00000":
		res += hash[5]
		print input+str(index), hash, res
	index+=1
	