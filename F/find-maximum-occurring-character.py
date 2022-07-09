import sys
from collections import Counter

input_str = ""

for line in sys.stdin:
    input_str += line

x = Counter(input_str.strip()).most_common(1)
print(x[0][0])