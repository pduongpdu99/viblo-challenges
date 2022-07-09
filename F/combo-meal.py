import sys
 
input_str = ""
 
for line in sys.stdin:
    input_str += line
 
lines = input_str.strip().split("\n")[1:]
for line in lines:
    b,s,c = map(int, line.strip().split(" "))
    print(b+s-c)