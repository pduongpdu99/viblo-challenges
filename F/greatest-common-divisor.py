import sys, math

input_str = ""

for line in sys.stdin:
    input_str += line

a,b = map(int, input_str.strip().split(" "))
print(math.gcd(a,b))
