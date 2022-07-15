import sys
import timeit
start = timeit.default_timer()

input_str = ""

for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    input_str += line


def addition(a, b):
    max_len = max(len(a), len(b))

    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    temp = 0

    for i in range(max_len - 1, - 1, - 1):
        num = int(a[i]) + int(b[i]) + temp
        if num % 2 == 0:
            result = '0' + result
        else:
            result = '1' + result

        if num == 2:
            temp = 1
        else:
            temp = 0

    if temp != 0:
        result = '01' + result

    if int(result) == 0:
        result = 0

    return result


def subtraction(a, b):
    max_len = max(len(a), len(b))

    a = a.zfill(max_len)
    b = b.zfill(max_len)

    result = ''
    temp = 0

    for i in range(max_len - 1, - 1, - 1):
        num = int(a[i]) - int(b[i]) - temp
        if num % 2 == 1:
            result = '1' + result
        else:
            result = '0' + result

        if num < 0:
            temp = 1
        else:
            temp = 0

    if temp != 0:
        result = '01' + result

    if int(result) == 0:
        result = 0

    return result


def division(a, b):
    result = ''
    temp = '0'
    r = 0

    for i in range(len(a)):
        if int(b) > int(temp):
            result += '0'
            temp += a[i]
        else:
            r = subtraction(temp, b)
            if r == 0:
                temp = a[i]
                result += '1'
            else:
                r = str(r).lstrip('0')
                result += '1'
                temp = r + a[i]

    if temp != int(0):
        result = result + '0'

    return result.lstrip("0")


if len(input_str) > 0 and input_str[0] == '0':
    input_str = input_str[1:][:10**6].strip()

# x = int(input_str[:10**6].strip(), 2)

c = 0
print(division(input_str, '10'))

while len(input_str) > 0 and input_str != '1':
    # thực hiện xét điều kiện
    if int(input_str, 2) % 2 == 1:
        input_str = addition(input_str, '1')
    else:
        input_str = division(input_str, '10')
    # đếm
    c += 1

print(c)

stop = timeit.default_timer()
print('Time: ', stop - start)
