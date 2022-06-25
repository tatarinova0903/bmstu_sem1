# Лежит ли отрезок полностью внутри прямоугольника
def isInside(x_start, x_end, x_left, x_right, y_start, y_end, y_bottom, y_top):
    if x_left <= x_start <= x_right and x_left <= x_end <= x_right and y_bottom <= y_start <= y_top and y_bottom <= y_end <= y_top:
        return True
    return False
    

# Найти точку пересечения прямых
def linesIntersection(A1, B1, C1, A2, B2, C2):
    delta = A1 * B2 - B1 * A2
    if delta == 0:
        return (None, None)
    else:
        delta_x = -C1 * B2 - B1 * (-C2)
        delta_y = A1 * (-C2) - (-C1) * A2 
        x = delta_x / delta
        y = delta_y / delta
        return (x, y)


# Лежит ли точка пересечения прямых на стороне прямоугольника и отрезке
def belongToPiece(coord1, bottom1, top1, coord2, bottom2, top2):
    if coord1 != None:
        if bottom1 > top1:
            bottom1, top1 = top1, bottom1
        if bottom2 > top2:
            bottom2, top2 = top2, bottom2
        if bottom1 <= coord1 <= top1 and bottom2 <= coord2 <= top2:
            return True
    return False


# Основная программа
input_file = open('input.txt')
output_file = open('output.txt', 'w')
N = int(input_file.readline())
for i in range(N):
    x_start, y_start, x_end, y_end, x_left, y_top, x_right, y_bottom = map(int, input_file.readline().split())
    
    intersection = False

    # Лежит ли отрезок полностью внутри прямоугольника
    if isInside(x_start, x_end, x_left, x_right, y_start, y_end, y_bottom, y_top):
        intersection = True
    else:
        # Уравнение прямой, содержащей отрезок
        A_line = y_start - y_end
        B_line = x_end - x_start
        C_line = x_start * y_end - x_end * y_start

        # Уравнение прямой, содержащей верхнюю сторону прямоугольника
        A_top_side = 0
        B_top_side = x_right - x_left
        C_top_side = x_left * y_top - x_right * y_top

        (x, y) = linesIntersection(A_line, B_line, C_line, A_top_side, B_top_side, C_top_side)
        intersection = belongToPiece(x, x_left, x_right, y, y_start, y_end)
        if not intersection:
            # Уравнение прямой, содержащей нижнюю сторону прямоугольника
            A_bottom_side = 0
            B_bottom_side = x_right - x_left
            C_bottom_side = x_left * y_bottom - x_right * y_bottom

            (x, y) = linesIntersection(A_line, B_line, C_line, A_bottom_side, B_bottom_side, C_bottom_side)
            intersection = belongToPiece(x, x_left, x_right, y, y_start, y_end)
            if not intersection:
                # Уравнение прямой, содержащей левую сторону прямоугольника
                A_left_side = y_top - y_bottom
                B_left_side = 0
                C_left_side = x_left * y_bottom - x_left * y_top

                (x, y) = linesIntersection(A_line, B_line, C_line, A_left_side, B_left_side, C_left_side)
                intersection = belongToPiece(y, y_bottom, y_top, x, x_start, x_end)

                if not intersection:
                    # Уравнение прямой, содержащей правую сторону прямоугольника
                    A_right_side = y_top - y_bottom
                    B_right_side = 0
                    C_right_side = x_right * y_bottom - x_right * y_top

                    (x, y) = linesIntersection(A_line, B_line, C_line, A_right_side, B_right_side, C_right_side)
                    intersection = belongToPiece(y, y_bottom, y_top, x, x_start, x_end)

    if intersection:
        output_file.write('T\n')
    else:
        output_file.write('F\n')

input_file.close()
output_file.close()