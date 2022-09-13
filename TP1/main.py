def find_rectangle():
    # The user gives us all the data we need to solve the problem
    l1, h1 = input().split()
    l = int(l1)
    h = int(h1)
    n = int(input())
    points = [(0, 0)]
    for i in range(0, int(n)):
        x, y = input().split()
        x = int(x)
        y = int(y)
        points.append((x, y))
    points.append((l, 0))
    # print('l :', l)
    # print('h :', h)
    # print('n :', n)
    # print('points :', points)

    area_max = 0
    points_best_rectangle = [(0, 0), (0, 0), (0, 0), (0, 0)]

    # n+2-1 for the 2 points we add and -1 because we are going to take 2 points to find a rectangle
    for i in range(0, n+1):
        (x1, y1) = points[i]
        (x2, y2) = points[i+1]
        result = h * (x2-x1)
        if result > area_max:
            area_max = result
            points_best_rectangle = [(x1, 0), (x1, h), (x2, h), (x2, 0)]

    # n because we take 3 points in the list to find a rectangle
    for i in range(0, n):
        (x1, y1) = points[i]
        (x2, y2) = points[i + 1]
        (x3, y3) = points[i + 2]
        result = y2 * (x3 - x1)
        if result > area_max:
            area_max = result
            points_best_rectangle = [(x1, 0), (x1, y2), (x3, y2), (x3, 0)]

    print(area_max)
    # print(points_best_rectangle)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    find_rectangle()
