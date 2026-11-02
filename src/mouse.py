import glfw

def get_mouse_state(HEIGHT, window):
    x, y = glfw.get_cursor_pos(window)
    pressed = glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS
    return int(x), int(HEIGHT - 1 - y), pressed