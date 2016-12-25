# -*- coding: utf-8 -*-
import re

lines = open("input.txt", "r").read().split("\n")

values = []
bots = [{} for i in range(1000)]

for line in lines:
    m = re.match(r"bot (\w+) gives low to (\w+) (\w+) and high to (\w+) (\w+)", line)
    if m: # it's a bot
	bot = {
	    "id": int(m.group(1)),
	    "gives_high_to_bot": (m.group(4) == "bot"),
	    "gives_high_to": int(m.group(5)),
	    "gives_low_to_bot": (m.group(2) == "bot"),
	    "gives_low_to": int(m.group(3)),
	    "value": None
	}
	bots[bot["id"]] = bot
    else: # it's a value
	m = re.match(r"value (\w+) goes to bot (\w+)", line)
	if not m: # this is for debug
	    print line
	    exit()
	val = int(m.group(1))
	bot_id = int(m.group(2))
	values.append((val,bot_id))
	
# if we've reached this point all bot-definitions are in the variable 'bots'

def give_value_to_bot(val, bot_id):
    if bots[bot_id]["value"]:
	if bots[bot_id]["value"] == 17 or bots[bot_id]["value"] == 61:
	    print "botid",bot_id,"val",val,"oldval",bots[bot_id]["value"]
	# check whats's higher and call give_value_to_bot 2 times. (or to_output)
	if val > bots[bot_id]["value"]:
	    h = val
	    l = bots[bot_id]["value"]
	else:
	    h = bots[bot_id]["value"]
	    l = val

	if bots[bot_id]["gives_high_to_bot"]:
	    give_value_to_bot(h, bots[bot_id]["gives_high_to"])
	else:
	    print "bot %i gives (high) %i to output %i" % (bot_id, h, bots[bot_id]["gives_high_to"])

	if bots[bot_id]["gives_low_to_bot"]:
	    give_value_to_bot(l, bots[bot_id]["gives_low_to"])
	else:
	    print "bot %i gives (low) %i to output %i" % (bot_id, l, bots[bot_id]["gives_low_to"])

    else:
	bots[bot_id]["value"] = val

for value, botid in values:
    give_value_to_bot(value, botid)
