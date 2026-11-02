import primitives
import mouse

def pencil(x, y, pressed, last_point, WIDTH, HEIGHT, COLOR, CANVAS):
    if not pressed:
        return None

    if last_point is None:
        primitives.set_pixel_color(x, y, WIDTH, HEIGHT, COLOR, CANVAS)
    else:
        primitives.draw_bresenham_line(last_point[0], last_point[1], x, y, WIDTH, HEIGHT, COLOR, CANVAS)

    return (x, y)

def erase(x, y, pressed, last_point, WIDTH, HEIGHT, CANVAS):
    return pencil(x, y, pressed, last_point, WIDTH, HEIGHT, [255,255,255], CANVAS)