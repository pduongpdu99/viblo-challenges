import sys
 
input_str = ""
 
for line in sys.stdin:
    input_str += line
 
ca = 0
c0 = 0
cd = 0
 
 
lines = input_str.strip().split("\n")
length = int(lines[0].strip())
nums = map(int, lines[1].strip().split(" "))
 
for i in nums:
    if i < 0:
        ca += 1
    if i == 0:
        c0 += 1
    if i > 0:
        cd += 1
 
print("{0:.6f}".format(cd/length))
print("{0:.6f}".format(ca/length))
print("{0:.6f}".format(c0/length))