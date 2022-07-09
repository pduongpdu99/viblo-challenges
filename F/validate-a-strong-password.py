import sys
import re

input_str = ""

for line in sys.stdin:
    input_str += line

x = []
x.append(8 <= len(input_str) <= 50)
x.append(max([i.islower() for i in input_str]))
x.append(max([i.isupper() for i in input_str]))
x.append(max([i.isdigit() for i in input_str]))
x.append(max([i in "!@#$%^&*()-_+." for i in input_str]))

print("false" if min(x) == False else "true")
