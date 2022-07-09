import sys

input_str = ""

for line in sys.stdin:
    input_str += line

f0 = 1
f1 = 1
fn = f0 + f1
n = int(input_str.strip())
for i in range(1, n):
    f0 = f1
    f1 = fn
    fn = f0 + f1

print(f0)