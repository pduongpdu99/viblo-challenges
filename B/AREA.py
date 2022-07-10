"""
5 6
-5 -1 1 2 5
-4 -3 -2 3 4 5
"""

# bỏ qua input
import sys
import math


input_str = """
5 6
-5 -1 1 2 5
-4 -3 -2 3 4 5
"""


def ip():
    global input_str
    for line in sys.stdin:
        if len(line.strip()) == 0:
            break
        input_str += line

    print(input_str)


def aspect_length(p0, p1):
    return int(math.sqrt(
        (p0[0] - p1[0])**2 + (p0[1] - p1[1])**2
    ))


def cal_rectangle_area(p0, p1, p2):
    aspect_one = aspect_length(p0, p1)
    aspect_two = aspect_length(p0, p2)
    return aspect_one * aspect_two


def presolve(st):
    return st.strip().split("\n")


def get_coords(rows, cols):
    """khởi tạo matrix dựa vào các điểm trên Oxy coordinate

    Args:
        rows (_type_): danh sách các điểm trên trục y -> sẽ dựng các đường thẳng theo hệ vuông góc
        cols (_type_): danh sách các điểm trên trục x -> sẽ dựng các đường thẳng theo hệ vuông góc
    """
    coords = []
    rowMax = max(rows)
    colMax = max(cols)
    rowMin = min(rows)
    colMin = min(cols)

    rowLen = rowMax - rowMin
    colLen = colMax - colMin

    # vị trí tọa độ O(0,0)
    p0 = [rowLen + rowMin, colLen - colMax]

    global startX
    startX = rowMax
    while startX >= rowMin:
        if startX in rows:
            startY = colMin
            while startY <= colMax:
                if startY in cols:
                    coords.append([startX, startY])
                startY += 1
        startX -= 1
    return coords


def get_matrix(coords):
    result = {}
    for coord in coords:
        if coord[0] not in result:
            result[coord[0]] = []

        result[coord[0]].append(coord)
    return result


def solve(lines):
    rows = list(map(int, lines[2].split(" ")))
    cols = list(map(int, lines[1].split(" ")))

    coords = list(get_matrix(get_coords(rows, cols)).values())
    for line in coords:
        print(line)

    tong = 0

    rowMax = len(rows)
    colMax = len(cols)
    for i in range(0, len(coords)):
        for j in range(0, len(coords[0])):
            print("area 1")
            print("[ ,   ]", coords[0][j])
            print(coords[i][0], coords[i][j])
            print()

            print("area 2")
            print(coords[i][0], coords[i][j])
            print("[ ,   ]", coords[rowMax - 1][j])
            print()

            print("area 3")
            print(coords[i][j], coords[i][colMax - 1])
            print(coords[rowMax - 1][j], "[ ,   ]")
            print()

            print("area 4")
            print(coords[0][j], "[ ,   ]")
            print(coords[i][j], coords[i][colMax - 1])
            print()

            area1 = cal_rectangle_area(
                coords[i][j], coords[i][0], coords[0][j])
            area2 = cal_rectangle_area(
                coords[i][j], coords[i][0], coords[rowMax - 1][j])
            area3 = cal_rectangle_area(
                coords[i][j], coords[rowMax - 1][j], coords[i][colMax - 1])
            area4 = cal_rectangle_area(
                coords[i][j], coords[0][j], coords[i][colMax - 1])
            tong += area1 + area2 + area3 + area4
            print(area1, area2, area3, area4)
            print("===================")
    print(tong)
    
    for line in coords:
        print(line)


pre = presolve(input_str)
solve(pre)
