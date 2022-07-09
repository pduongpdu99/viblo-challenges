import sys

input_str = ""

for line in sys.stdin:
    input_str += line

print(sum(map(int, input_str.strip().split(" "))))
