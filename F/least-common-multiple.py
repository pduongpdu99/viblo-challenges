import sys,math

input_str = ""

def lcd(a,b):
    return abs(a*b) // math.gcd(a,b)

for line in sys.stdin:
    input_str += line

a,b = map(int, input_str.strip().split(" "))
print(lcd(a,b))