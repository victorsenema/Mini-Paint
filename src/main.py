import glfw
from OpenGL.GL import *
import numpy as np

import primitives
import mouse
import tool
import menu

#CANVAS
HEIGHT, WIDTH = 600, 500
CANVAS = np.full((HEIGHT, WIDTH, 3), 255, dtype=np.uint8)

#MENU
DRAW_HEIGHT = HEIGHT - menu.get_menu_height()  

#COLORS
COLOR_PALETTE = {
                "BLACK":    [80, 80, 80],
                "WHITE":    [255, 255, 255],
                "RED":      [255, 179, 186],
                "GREEN":    [183, 228, 199],
                "BLUE":     [174, 198, 255],
                "YELLOW":   [255, 255, 186],
                "CYAN":     [178, 235, 242],
                "MAGENTA":  [244, 194, 230],
                }
SELECTED_COLOR = COLOR_PALETTE["BLACK"]

# TOOL
SELECTED_TOOL = "PEN"

# BRUSH
SELECTED_BRUSH = "SMALL"
BRUSH_MASKS = {
    "SMALL":  [[1]],

    "MEDIUM": [[0,1,0],
               [1,1,1],
               [0,1,0]],

    "BIG":    [[0,1,1,1,0],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [1,1,1,1,1],
               [0,1,1,1,0]],
}

# How each tool uses the tool
DRAG_TOOLS = ["PEN", "ERASER", "LINE_BRESEHAM", "RECTANGLE_HOLLOW", "RECTANGLE_FILLED", "CIRCLE_HOLLOW", "CIRCLE_FILLED"]
CLICK_TOOLS = {"CURVE": 4, "BUCKET": 1, "COLOR_PICKER": 1} #clicks needed

#MOUSE
LAST_MOUSE_COORDINATE = None

#draw functions
def draw_triangle():
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0, 0)
    glVertex2f(0.5, -0.5)
    glEnd()


def create_window(width, height):
    if not glfw.init():
       return None
    window = glfw.create_window( width, height, "Mini Paint", None, None )

    if not window:
        glfw.terminate()
        return None
    
    glfw.make_context_current(window)
    return window

    return window

def select_from_menu(x, y, button_areas, color_areas, brush_areas):
    global SELECTED_TOOL, SELECTED_COLOR, SELECTED_BRUSH

    brush_name = menu.find_clicked_button(x, y, brush_areas)
    if brush_name is not None:
        if brush_name != SELECTED_BRUSH:
            menu.change_selected_brush(SELECTED_BRUSH, brush_name, WIDTH, HEIGHT, CANVAS)
            SELECTED_BRUSH = brush_name
        return False

    color_name = menu.find_clicked_button(x, y, color_areas)
    if color_name is not None:
        SELECTED_COLOR = COLOR_PALETTE[color_name]
        return False

    button_name = menu.find_clicked_button(x, y, button_areas)

    if button_name == "NEW":
        tool.new(WIDTH, DRAW_HEIGHT, CANVAS)
        return False

    if button_name == "SAVE":
        path = tool.ask_save_path()
        if path:
            tool.save(WIDTH, DRAW_HEIGHT, CANVAS, path)
        return False

    if button_name is None or button_name in menu.ACTION_BUTTONS or button_name == SELECTED_TOOL:
        return False

    menu.change_selected_tool(SELECTED_TOOL, button_name, WIDTH, HEIGHT, CANVAS)
    SELECTED_TOOL = button_name
    return True

def update(window):
    global SELECTED_COLOR

    last_point = None
    drag_start = None
    snapshot = None
    click_points = []
    was_pressed = False
    was_drawing = False
    ignore_until_release = False

    menu.draw_menu(WIDTH, HEIGHT, CANVAS, COLOR_PALETTE, SELECTED_TOOL, SELECTED_BRUSH)
    button_areas = menu.get_button_areas(HEIGHT)
    color_areas = menu.get_color_areas(HEIGHT)
    brush_areas = menu.get_brush_areas(HEIGHT)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)

        x, y, pressed = mouse.get_mouse_state(HEIGHT, window)

        # MENU BAR onlyu clicks
        if pressed and not was_pressed and y >= DRAW_HEIGHT:
            ignore_until_release = True
            if select_from_menu(x, y, button_areas, color_areas, brush_areas):
                last_point = None
                drag_start = None
                snapshot = None
                click_points = []
        if not pressed:
            ignore_until_release = False
        was_pressed = pressed

        drawing = pressed and not ignore_until_release
        mask = BRUSH_MASKS[SELECTED_BRUSH]

        if SELECTED_TOOL == "PEN":
            last_point = tool.pencil(x, y, drawing, last_point, WIDTH, DRAW_HEIGHT, SELECTED_COLOR, CANVAS, mask)

        elif SELECTED_TOOL == "ERASER":
            last_point = tool.erase(x, y, drawing, last_point, WIDTH, DRAW_HEIGHT, CANVAS, mask)

        elif SELECTED_TOOL in tool.SHAPES:
            start = drag_start
            drag_start, phase = mouse.drag(x, y, drawing, drag_start)
            if phase == "START":
                start = drag_start
                snapshot = CANVAS.copy()
            if phase is not None:
                CANVAS[:] = snapshot
                tool.draw_shape(SELECTED_TOOL, start, (x, y), phase != "END", WIDTH, DRAW_HEIGHT, SELECTED_COLOR, CANVAS, mask)

        elif SELECTED_TOOL in CLICK_TOOLS:
            click_points, done = mouse.click(x, y, drawing, was_drawing, click_points, CLICK_TOOLS[SELECTED_TOOL])
            if done:
                click_x, click_y = click_points[0]
                if SELECTED_TOOL == "BUCKET":
                    tool.bucket(click_x, click_y, WIDTH, DRAW_HEIGHT, SELECTED_COLOR, CANVAS)
                elif SELECTED_TOOL == "COLOR_PICKER":
                    SELECTED_COLOR = tool.color_picker(click_x, click_y, WIDTH, DRAW_HEIGHT, CANVAS)
                elif SELECTED_TOOL == "CURVE":
                    p1, p2, p3, p4 = click_points
                    primitives.draw_bezier_curve(p1, p2, p3, p4, WIDTH, DRAW_HEIGHT, SELECTED_COLOR, CANVAS, mask)
                click_points = []

        was_drawing = drawing

        glRasterPos2f(-1, -1)
        glDrawPixels(WIDTH, HEIGHT, GL_RGB, GL_UNSIGNED_BYTE, CANVAS)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    window = create_window(WIDTH, HEIGHT)
    update(window)