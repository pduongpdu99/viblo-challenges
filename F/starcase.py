import sys
 
input_str = ""
 
for line in sys.stdin:
    input_str += line
 
line_num = int(input_str.strip())
index = 1
while index <= line_num:
    print((line_num - index)*" "+"#"*index)
    index += 1