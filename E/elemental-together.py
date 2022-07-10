import sys, math

input_str = ""

for line in sys.stdin:
    input_str += line

def is_prime(x):
    if x < 2:
        return False

    if x == 2 or x == 3:
        return True
    
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

lines = input_str.strip().split("\n")

for line in lines[1:]:
    count = 0
    num = int(line.strip())
        
    for k in range(1, num+1):
        if math.gcd(k, num) == 1:
            count += 1
    print(1 if is_prime(count) else 0)
