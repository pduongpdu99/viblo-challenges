import sys

input_str = ""

for line in sys.stdin:
    input_str += line

a, b = map(int, input_str.strip().split(" "))

if a == 0 and a == b:
    print(-1)
elif a == 0 and b == 1:
    print("1")
else:
    if a - b > 1:
        print(-1)
    else:
        if a - b == 1:
            print("0" + "10"*b)
        elif a == b:
            print("10"*a)
        else:
            is_cancel = False

            if not is_cancel:
                x = []
                t = b-a
                for i in range(t):
                    if a == 0:
                        if b == 2:
                            x.append("11")
                            b -= 2
                        if b == 1:
                            x.append("1")
                            b -= 1
                        if b > 2:
                            print(-1)
                            is_cancel = True
                        break

                    if a < 0:
                        print(-1)
                        is_cancel = True
                        break
                    x.append("11")
                    x.append("0")
                    b -= 2
                    a -= 1

            if not is_cancel:
                for i in range(b):
                    x.append("1")
                    x.append("0")
                    a -= 1
                    b -= 1
                print("".join(x))
