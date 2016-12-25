# -*- coding: utf-8 -*-
import re

lines = open("input.txt", "r").read().split("\n")

re_outside_brackets = r"(\w)(?!\1)(\w)\2\1"
re_inside_brackets  = r"\[\w*(\w)(?!\1)(\w)\2\1\w*\]"

support_tls = [ line for line in lines if not re.search(re_inside_brackets, line) ] # the order matters
support_tls = [ line for line in support_tls if re.search(re_outside_brackets, line) ] # the order matters

print len(support_tls)
