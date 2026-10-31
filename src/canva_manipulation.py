def set_pixel(x, y, WIDTH, HEIGHT, color, canvas):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        canvas[x,y] = color

def draw_bresenham_line(x1, y1, x2, y2, WIDTH, HEIGHT, color, canvas):
    dx = x2 - x1
    dy = y2 - y1

    x = x1
    y = y1

    p = 2 * dy - dx

    while x <= x2:
        set_pixel(x, y, WIDTH, HEIGHT, color, canvas)

        if p < 0:
            p = p + 2 * dy
        else:
            y = y + 1
            p = p + 2 * dy - 2 * dx

        x = x + 1

def dda():
    return 1

def draw_rectangle_hollow(x1, y1, x2, y2, WIDTH, HEIGHT, color, canvas):
    for x in range(x1,x2):
        set_pixel(x, y1, WIDTH, HEIGHT, color, canvas)
        set_pixel(x, y2, WIDTH, HEIGHT, color, canvas)

    for y in range(y1,y2):
        set_pixel(x1, y, WIDTH, HEIGHT, color, canvas)
        set_pixel(x2, y, WIDTH, HEIGHT, color, canvas)

def draw_rectangle_filled(x1, y1, x2, y2, WIDTH, HEIGHT, color, canvas):
    for x in range(x1,x2):
        for y in range(y1,y2):
            set_pixel(x, y, WIDTH, HEIGHT, color, canvas)

def draw_simetric_points(x, y, x_displacement, y_displacement, WIDTH, HEIGHT, color, canvas):
    set_pixel(x + x_displacement, y + y_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x - x_displacement, y + y_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x + x_displacement, y - y_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x - x_displacement, y - y_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x + y_displacement, y + x_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x - y_displacement, y + x_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x + y_displacement, y - x_displacement, WIDTH, HEIGHT, color, canvas)
    set_pixel(x - y_displacement, y - x_displacement, WIDTH, HEIGHT, color, canvas)

def draw_circle_hollow(x, y, r, WIDTH, HEIGHT, color, canvas):
    x_displacement = 0
    y_displacement = r
    p_decision = 1 - r

    draw_simetric_points(x, y, x_displacement, y_displacement, WIDTH, HEIGHT, color, canvas)

    while y_displacement > x_displacement:
        x_displacement += 1

        if p_decision < 0:
            p_decision += (2 * x_displacement) + 1
        else:
            y_displacement -= 1
            p_decision += 2 * (x_displacement - y_displacement) + 1

        draw_simetric_points(x, y, x_displacement, y_displacement, WIDTH, HEIGHT, color, canvas)

def draw_circle_filled(x, y, r, WIDTH, HEIGHT, color, canvas):
    x_displacement = 0
    y_displacement = r
    m_decision = 5 - (4 * r)

    while x_displacement <= y_displacement:
        draw_bresenham_line(x - x_displacement, y - y_displacement, x + x_displacement, y - y_displacement, WIDTH, HEIGHT, color, canvas)
        draw_bresenham_line(x - x_displacement, y + y_displacement, x + x_displacement, y + y_displacement, WIDTH, HEIGHT, color, canvas)
        draw_bresenham_line(x - y_displacement, y - x_displacement, x + y_displacement, y - x_displacement, WIDTH, HEIGHT, color, canvas)
        draw_bresenham_line(x - y_displacement, y + x_displacement, x + y_displacement, y + x_displacement, WIDTH, HEIGHT, color, canvas)

        if m_decision > 0:
            y_displacement -= 1
            m_decision -= 8 * y_displacement

        x_displacement = x_displacement + 1
        m_decision = m_decision + (8 * x_displacement) + 4