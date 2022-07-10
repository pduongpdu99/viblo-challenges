import sys

input_str = ""

for line in sys.stdin:
    input_str += line

nums = map(int, input_str.strip().split("\n")[1].split(" "))
for num in nums:
    c = 0
    for i in range(2, num):
        if num % i == 0:
            c += 1
    print("YES" if c == 1 else "NO")
