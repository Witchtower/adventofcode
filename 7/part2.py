# -*- coding: utf-8 -*-
import re

lines = open("input.txt", "r").read().split("\n")

brackets_second = r"(\w)(?!\1)(\w)\1\w*(?:\[\w*\]\w*)*(?=\[\w*\2\1\2)"
brackets_first = r"\[\w*(\w)(?!\1)(\w)\1(?=\w*\]\w*(?:\[\w*\]\w*)*\2\1\2.*)"

sll_ips = [i for i in lines if re.search(brackets_second, i) or re.search(brackets_first, i)]

print len(sll_ips)
