import sys
import math

input_str = ""

for line in sys.stdin:
    input_str += line


def tong_chu_so(x: int):
    r = 0
    while x > 0:
        r += x % 10
        x //= 10
    return r


num = int(input_str.strip())
lim = int(math.sqrt(num))

best = num
bestSum = tong_chu_so(num)

for i in range(1, lim + 1):
    if num % i == 0:
        tong = tong_chu_so(i)
        if tong > bestSum or tong == bestSum and i < best:
            bestSum = tong
            best = i

        tong = tong_chu_so(num//i)
        if tong > bestSum or tong == bestSum and num//i < best:
            bestSum = tong
            best = num//i

print(best)
