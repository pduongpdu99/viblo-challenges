import sys

input_str = ""

for line in sys.stdin:
    input_str += line

num = int(input_str.strip())
if num > 0:
    if num % 400 == 0 or (num % 4 == 0 and num % 100 != 0):
        print("true")
    else:
        print("false")
else:
    print("false")
