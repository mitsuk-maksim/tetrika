def intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    # x1, y1, x2, y2 - левый прямоугольник
    # x3, y3, x4, y4 - правый прямоугольник

    # сделаем так, что х1, y1, x3,y3 - левый верхний угол

    if x2 < x1 and y2 < y1:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    if x4 < x3 and y4 < y3:
        x3, x4 = x3, x4
        y3, y4 = y3, y4

    ax1 = x1
    ay1 = y2
    ax2 = x2
    ay2 = y1

    bx1 = x3
    by1 = y4
    bx2 = x4
    by2 = y3
    # s1 = (x1 >= x3 and x1 <= x4) or (x2 >= x3 and x2 <= x4)
    # s2 = (y1 >= y3 and y1 <= y4) or (y2 >= y3 and y2 <= y4)
    # s3 = (x3 >= x1 and x3 <= x2) or (x4 >= x1 and x4 <= x2)
    # s4 = (y3 >= y1 and y3 <= y2) or (y4 >= y1 and y4 <= y2)
    #
    # if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
    #     return True
    # else:
    #     return False

    s1 = (ax1 >= bx1 and ax1 <= bx2) or (ax2 >= bx1 and ax2 <= bx2)
    s2 = (ay1 >= by1 and ay1 <= by2) or (ay2 >= by1 and ay2 <= by2)
    s3 = (bx1 >= ax1 and bx1 <= ax2) or (bx2 >= ax1 and bx2 <= ax2)
    s4 = (by1 >= ay1 and by1 <= ay2) or (by2 >= ay1 and by2 <= ay2)

    if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
        return True
    else:
        return False

print(intersection(1,5,6,2,3,4,9,4))
