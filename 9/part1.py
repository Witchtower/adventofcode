# -*- coding: utf-8 -*-
import re
inp = open("input_test.txt", "r").read()

def unpack(inp_str):
    res = ""
    m = re.search(r"\(([0-9]+)x([0-9]+)\)", inp_str) 
    if not m:
	return inp_str
    l = m.group(1)
    t = m.group(2)
    ss = "(%sx%s)" % (l, t)
    pos = inp_str.index(ss)
    pre = inp_str[:pos]
    rep = inp_str[pos+len(ss):pos+len(ss)+int(l)]
    res += int(t) * rep
    # print inp_str[:pos], "--", ss, "--", rep, "---", inp_str[pos+len(ss)+len(rep):]
    return pre + unpack(res+inp_str[pos+len(ss)+len(rep):])



print unpack(inp)
