import sys

input_str = ""

for line in sys.stdin:
    input_str += line

print("true" if int(input_str.strip()) % 2 == 0 else "false")
