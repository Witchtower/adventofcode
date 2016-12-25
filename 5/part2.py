from hashlib import md5

input = "reyedfim"

index = 0

res = ["*" for i in range(8)]

while "*" in res:
	hash = md5(input+str(index)).hexdigest()
	#print hash, hash[:5]
	if hash[:5] == "00000" and ord(hash[5]) in range(ord("0"), ord("8")):
		res[int(hash[5])] = hash[6]
		print input+str(index), hash, "".join(res)
	index+=1
	
# don't overwrite the positions once they're set.
# i got the output:
"""
reyedfim1617991  00000774278f87486dd763de7c36d7ac *******7
reyedfim2564359  000003dbf0ad65c48ec74313dde4ea8d ***d***7
reyedfim2834991  000005e7d422c718d47e47dfff429cbb ***d*e*7
reyedfim3605750  000004d93de3e18869925a23989f0753 ***dde*7
reyedfim10105659 0000035e9b177813caa7bd6b8569e35f ***5de*7
reyedfim11395933 000005195dd68e94d60bb8e4f3f3821e ***5d1*7
reyedfim12187005 000000832f3a209acfbdfe86964ced01 8**5d1*7
reyedfim13432325 0000023c990be097d3ec134b259cc95d 8*35d1*7
reyedfim19897122 0000000c332c7c8e538f615cc7c90f03 0*35d1*7
reyedfim21679503 00000160ed216eb038fb450fb38bb34f 0635d1*7
reyedfim21842490 000005645186fa754e750ba424ccdba3 0635d6*7
reyedfim23090544 000000ea8d5741da3a282312b391fe4a e635d6*7
reyedfim25067104 000006274ce1d3978e2396f6456c4adc e635d627
"""

# and took the uppermost numbers for every column to get the right answer

# right answer: 863dde27