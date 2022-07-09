import sys

input_str = ""

for line in sys.stdin:
    input_str += line

nums = list(map(int, input_str.strip().split(" ")))

if len(nums) > 0:
    _min = min(nums)
    _max = max(nums)

    rs = []
    # Độ phức tạp: O(n)
    for i in range(_min, _max + 1):
        if i not in nums:
            rs.append(i)
    print(" ".join(map(str, rs)))
