import sys

input_str = ""

for line in sys.stdin:
    input_str += line


def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    return prime


lines = input_str.strip().split("\n")[1:]
for line in lines:
    a, b = map(int, line.strip().split(" "))
    sang = SieveOfEratosthenes(b)
    c = 0
    for i in range(a, len(sang)-6):
        if sang[i] and sang[i+6]:
            c += 1
        else:
            continue

    print(c)
