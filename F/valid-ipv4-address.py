import sys
import re

input_str = ""


def ipv4(s):
    pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    test = pat.match(s)
    print("Valid" if test else "Invalid")


for line in sys.stdin:
    input_str += line

ipv4(input_str.strip())
