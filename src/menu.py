import primitives

# COLORS
BACKGROUND_COLOR = [39, 39, 39]
BUTTOM_BORDER_COLOR = [20, 20, 20]
BUTTOM_BACKGROUND = [60, 60, 60]
SELECTED_BUTTON_BACKGROUND = [30, 30, 30]
ICON_COLOR = [130, 130, 130]

# BUTTONS
MENU_STRUCTURE = [  ["PEN",              "ERASER"],
                    ["BUCKET",           "COLOR_PICKER"],
                    ["LINE_BRESEHAM",    "CURVE"],
                    ["CIRCLE_HOLLOW",    "CIRCLE_FILLED"],
                    ["RECTANGLE_HOLLOW", "RECTANGLE_FILLED"]]

ACTION_STRUCTURE = [["NEW", "SAVE"]]
ACTION_BUTTONS = ["NEW", "SAVE"]

COLOR_PALLETE_STRUCTURE = [ ["BLACK",    "WHITE"],
                            ["RED",      "GREEN"],
                            ["BLUE",     "YELLOW"],
                            ["CYAN",     "MAGENTA"]]

BRUSH_SIZE = [ ["SMALL","MEDIUM", "BIG"]]
BRUSH_RADIUS = {"SMALL": 2, "MEDIUM": 4, "BIG": 7}


# BUTTON DEFINITIONS
BUTTON_SIZE = 15
BRUSH_BUTTON_SIZE = 20
MARGING = 10
GAP_BETWEEN_MENU_TOOLS = 40 
BRUSH_SIZE_MARGIN = 20

# BUTTON ICONS (0 = BUTTOM_BACKGROUND, 1 = ICON_COLOR)

BACKGROUND_ICON = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

PENCIL_ICON = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,1,0,0,0,0,0],
                [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

ERASE_ICON = [  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

BUCKET_ICON = [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
                [0,0,0,1,1,1,0,0,0,1,0,0,0,0,0],
                [0,0,1,1,1,0,0,0,0,1,0,0,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,1,0,0,0,0],
                [0,1,1,1,0,1,0,0,0,0,1,0,0,0,0],
                [0,0,1,1,0,1,0,0,0,0,0,1,0,0,0],
                [0,0,1,1,0,0,1,0,0,0,0,1,0,0,0],
                [0,0,0,1,1,0,1,0,0,0,0,0,1,0,0],
                [0,0,0,1,1,0,0,1,0,0,0,0,1,0,0],
                [0,0,0,1,1,0,0,1,0,0,1,1,0,0,0],
                [0,0,1,1,1,0,0,0,1,1,0,0,0,0,0],
                [0,1,1,1,1,1,0,1,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

COLOR_PICKER_ICON = [   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0],
                        [0,0,0,0,0,0,0,0,0,1,1,1,1,0,0],
                        [0,0,0,0,0,0,0,0,1,1,1,1,1,0,0],
                        [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],
                        [0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
                        [0,0,0,0,0,0,1,0,0,1,0,0,0,0,0],
                        [0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
                        [0,0,0,0,1,1,0,1,0,0,0,0,0,0,0],
                        [0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                        [0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],
                        [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

CURVE_ICON =      [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
                    [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],
                    [0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
                    [0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
                    [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

SAVE_ICON = [   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,1,0,0,1,0,0,0,0,0,1,0,0,1,0],
                [0,1,0,0,1,0,0,0,0,0,1,0,0,1,0],
                [0,1,0,0,1,1,1,1,1,1,1,0,0,1,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,1,0,0,1,1,1,1,1,1,1,0,0,1,0],
                [0,1,0,0,1,1,1,1,1,1,1,0,0,1,0],
                [0,1,0,0,1,1,1,1,1,1,1,0,0,1,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

NEW_ICON =    [ [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

LINE_ICON = [   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

def get_menu_height():
    buttons_per_group = len(MENU_STRUCTURE[0])
    return buttons_per_group * BUTTON_SIZE + (buttons_per_group + 1) * MARGING

def get_pallete_x_start():
    return MARGING + len(MENU_STRUCTURE) * (BUTTON_SIZE + MARGING) + GAP_BETWEEN_MENU_TOOLS

def get_brush_x_start():
    return get_pallete_x_start() + len(COLOR_PALLETE_STRUCTURE) * (BUTTON_SIZE + MARGING) + GAP_BETWEEN_MENU_TOOLS

def get_action_x_start():
    return get_brush_x_start() + len(BRUSH_SIZE[0]) * (BRUSH_BUTTON_SIZE + MARGING) + GAP_BETWEEN_MENU_TOOLS

def get_structures():
    return [(MENU_STRUCTURE, MARGING), (COLOR_PALLETE_STRUCTURE, get_pallete_x_start()), (ACTION_STRUCTURE, get_action_x_start())]

def get_button_rect(name, HEIGHT):
    for structure, x_start in get_structures():
        for group, line in enumerate(structure):
            if name in line:
                position = line.index(name)
                x1 = x_start + group * (BUTTON_SIZE + MARGING)
                x2 = x1 + BUTTON_SIZE - 1
                y2 = HEIGHT - MARGING - 1 - position * (BUTTON_SIZE + MARGING)
                y1 = y2 - BUTTON_SIZE + 1
                return x1, y1, x2, y2
    raise ValueError(f"botão '{name}' não está na MENU_STRUCTURE nem na COLOR_PALLETE_STRUCTURE")

def get_areas(structure, HEIGHT):
    areas = []
    for line in structure:
        for name in line:
            if name is None:
                continue
            areas.append((name, get_button_rect(name, HEIGHT)))
    return areas

def get_button_areas(HEIGHT):
    return get_areas(MENU_STRUCTURE + ACTION_STRUCTURE, HEIGHT)

def get_color_areas(HEIGHT):
    return get_areas(COLOR_PALLETE_STRUCTURE, HEIGHT)

def get_brush_rect(name, HEIGHT):
    position = BRUSH_SIZE[0].index(name)
    x1 = get_brush_x_start() + position * (BRUSH_BUTTON_SIZE + MARGING)
    x2 = x1 + BRUSH_BUTTON_SIZE - 1
    y2 = HEIGHT - BRUSH_SIZE_MARGIN - 1
    y1 = y2 - BRUSH_BUTTON_SIZE + 1
    return x1, y1, x2, y2

def get_brush_areas(HEIGHT):
    return [(name, get_brush_rect(name, HEIGHT)) for name in BRUSH_SIZE[0]]

def find_clicked_button(x, y, areas):
    for name, (x1, y1, x2, y2) in areas:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return name
    return None

# DRAW ICONS
def draw_icon(bitmap, left, top, WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    for i in range(len(bitmap)):
        for j in range(len(bitmap[0])):
            color = ICON_COLOR if bitmap[i][j] == 1 else background
            primitives.set_pixel_color(left + j, top - i, WIDTH, HEIGHT, color, CANVAS)

def draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS):
    primitives.draw_rectangle_hollow(x1 - 1, y1 - 1, x2 + 1, y2 + 1, WIDTH, HEIGHT, BUTTOM_BORDER_COLOR, CANVAS)


def draw_pen(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("PEN", HEIGHT)
    draw_icon(PENCIL_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_erase(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("ERASER", HEIGHT)
    draw_icon(ERASE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_bucket(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("BUCKET", HEIGHT)
    draw_icon(BUCKET_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_color_picker(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("COLOR_PICKER", HEIGHT)
    draw_icon(COLOR_PICKER_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_line_breseham(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("LINE_BRESEHAM", HEIGHT)
    draw_icon(LINE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_line_dda(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("LINE_DDA", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_curve(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("CURVE", HEIGHT)
    draw_icon(CURVE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_circle_hollow(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("CIRCLE_HOLLOW", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = BUTTON_SIZE // 2 - 1                                  # 6
    primitives.draw_circle_hollow(center_x, center_y, radius, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_circle_filled(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("CIRCLE_FILLED", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = BUTTON_SIZE // 2 - 1                                  # 6
    primitives.draw_circle_filled(center_x, center_y, radius, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_rectangle_hollow(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("RECTANGLE_HOLLOW", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    primitives.draw_rectangle_hollow(x1 + 1, y1 + 1, x2 - 1, y2 - 1, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_rectangle_filled(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("RECTANGLE_FILLED", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    # o draw_rectangle_filled não pinta x2/y2 (range exclui o último), então x2 e y2 do botão servem de limite
    primitives.draw_rectangle_filled(x1 + 1, y1 + 1, x2, y2, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_save(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("SAVE", HEIGHT)
    draw_icon(SAVE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_new(WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_button_rect("NEW", HEIGHT)
    draw_icon(NEW_ICON, x1, y2, WIDTH, HEIGHT, CANVAS, background)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_brush_button(name, WIDTH, HEIGHT, CANVAS, background=BUTTOM_BACKGROUND):
    x1, y1, x2, y2 = get_brush_rect(name, HEIGHT)
    primitives.draw_rectangle_filled(x1, y1, x2 + 1, y2 + 1, WIDTH, HEIGHT, background, CANVAS)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    primitives.draw_circle_filled(center_x, center_y, BRUSH_RADIUS[name], WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def change_selected_brush(old_brush, new_brush, WIDTH, HEIGHT, CANVAS):
    draw_brush_button(old_brush, WIDTH, HEIGHT, CANVAS)
    draw_brush_button(new_brush, WIDTH, HEIGHT, CANVAS, SELECTED_BUTTON_BACKGROUND)

DRAW_FUNCTIONS = {
    "PEN":              draw_pen,
    "ERASER":           draw_erase,
    "BUCKET":           draw_bucket,
    "CURVE":            draw_curve,
    "LINE_BRESEHAM":    draw_line_breseham,
    "LINE_DDA":         draw_line_dda,
    "CIRCLE_HOLLOW":    draw_circle_hollow,
    "CIRCLE_FILLED":    draw_circle_filled,
    "RECTANGLE_HOLLOW": draw_rectangle_hollow,
    "RECTANGLE_FILLED": draw_rectangle_filled,
    "COLOR_PICKER":     draw_color_picker,
    "SAVE":             draw_save,
    "NEW":              draw_new
}

def draw_color_pallete_buttons(name, color, WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect(name, HEIGHT)
    primitives.draw_rectangle_filled(x1, y1, x2 + 1, y2 + 1, WIDTH, HEIGHT, color, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def find_clicked_button(x, y, button_areas):
    for name, (x1, y1, x2, y2) in button_areas:
        if x1 <= x <= x2 and y1 <= y <= y2:
            return name
    return None

def draw_menu(WIDTH, HEIGHT, CANVAS, COLOR_PALLETE, selected_tool, selected_brush="SMALL"):
    DRAW_HEIGHT = HEIGHT - get_menu_height()
    primitives.draw_rectangle_filled(0, DRAW_HEIGHT, WIDTH, HEIGHT, WIDTH, HEIGHT, BACKGROUND_COLOR, CANVAS)

    for line in MENU_STRUCTURE + ACTION_STRUCTURE:
        for name in line:
            if name is None:
                continue
            if name == selected_tool:
                DRAW_FUNCTIONS[name](WIDTH, HEIGHT, CANVAS, SELECTED_BUTTON_BACKGROUND)
            else:
                DRAW_FUNCTIONS[name](WIDTH, HEIGHT, CANVAS)

    for line in COLOR_PALLETE_STRUCTURE:
        for name in line:
            if name is None:
                continue
            draw_color_pallete_buttons(name, COLOR_PALLETE[name], WIDTH, HEIGHT, CANVAS)

    for name in BRUSH_SIZE[0]:
        if name == selected_brush:
            draw_brush_button(name, WIDTH, HEIGHT, CANVAS, SELECTED_BUTTON_BACKGROUND)
        else:
            draw_brush_button(name, WIDTH, HEIGHT, CANVAS)

def change_selected_tool(old_tool, new_tool, WIDTH, HEIGHT, CANVAS):
    DRAW_FUNCTIONS[old_tool](WIDTH, HEIGHT, CANVAS)
    DRAW_FUNCTIONS[new_tool](WIDTH, HEIGHT, CANVAS, SELECTED_BUTTON_BACKGROUND)

