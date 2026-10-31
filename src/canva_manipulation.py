def set_pixel(x, y, WIDTH, HEIGHT, color, canvas):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        canvas[x,y] = color