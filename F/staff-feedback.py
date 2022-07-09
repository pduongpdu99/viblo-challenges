import sys

input_str = ""

for line in sys.stdin:
    input_str += line

counter = input_str.count(':))')*4
input_str = input_str.replace(':))', '')
counter += input_str.count(':)')*2
input_str = input_str.replace(':)', '')
counter += input_str.count(':((')*(-5)
input_str = input_str.replace(':((', '')
counter += input_str.count(':(')*(-1)
input_str = input_str.replace(':(', '')

print(counter)
