import glfw

def get_mouse_state(HEIGHT, window):
    x, y = glfw.get_cursor_pos(window)
    pressed = glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS
    return int(x), int(HEIGHT - 1 - y), pressed


def drag(x, y, pressed, start):
    if pressed and start is None:
        return (x, y), "START"
    if pressed:
        return start, "DRAG"
    if start is not None:
        return None, "END"
    return None, None

def click(x, y, pressed, was_pressed, points, needed):
    if pressed and not was_pressed:
        points = points + [(x, y)]
    return points, len(points) >= needed


