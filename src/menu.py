import primitives

# COLORS
BACKGROUND_COLOR = [39, 39, 39]
BUTTOM_BORDER_COLOR = [20, 20, 20]
BUTTOM_BACKGROUN = [60, 60, 60]
ICON_COLOR = [130, 130, 130]

MENU_STRUCTURE = [  ["PEN",              "ERASER"],
                    ["BUCKET",              "COLOR_PICKER"],
                    ["LINE_BRESEHAM",    "CURVE"],
                    ["CIRCLE_HOLLOW",    "CIRCLE_FILLED"],
                    ["RECTANGLE_HOLLOW", "RECTANGLE_FILLED"],
                    ["BLACK",            "WHITE"],
                    ["RED",              "GREEN"],
                    ["BLUE",             "YELLOW"],
                    ["CYAN",             "MAGENTA"],
                    ["NEW",             "SAVE"]]


# BUTTON DEFINITIONS
BUTTON_SIZE = 15
MARGING = 10

# BUTTON ICONS (0 = BUTTOM_BACKGROUN, 1 = ICON_COLOR)

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

def get_menu_height():
    buttons_per_group = len(MENU_STRUCTURE[0])
    return buttons_per_group * BUTTON_SIZE + (buttons_per_group + 1) * MARGING

def get_button_rect(name, HEIGHT):
    for group, line in enumerate(MENU_STRUCTURE):
        if name in line:
            position = line.index(name)
            x1 = MARGING + group * (BUTTON_SIZE + MARGING)
            x2 = x1 + BUTTON_SIZE - 1
            y2 = HEIGHT - MARGING - 1 - position * (BUTTON_SIZE + MARGING)
            y1 = y2 - BUTTON_SIZE + 1
            return x1, y1, x2, y2
    raise ValueError(f"botão '{name}' não está na MENU_STRUCTURE")

def get_button_at(x, y, HEIGHT):
    for line in MENU_STRUCTURE:
        for name in line:
            if name is None:
                continue
            x1, y1, x2, y2 = get_button_rect(name, HEIGHT)
            if x1 <= x <= x2 and y1 <= y <= y2:
                return name
    return None


# HELPERS DE DESENHO
def draw_icon(bitmap, left, top, WIDTH, HEIGHT, CANVAS):
    for i in range(len(bitmap)):
        for j in range(len(bitmap[0])):
            color = ICON_COLOR if bitmap[i][j] == 1 else BUTTOM_BACKGROUN
            primitives.set_pixel_color(left + j, top - i, WIDTH, HEIGHT, color, CANVAS)

def draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS):
    # moldura de 1 pixel logo FORA do botão, dentro da margem
    primitives.draw_rectangle_hollow(x1 - 1, y1 - 1, x2 + 1, y2 + 1, WIDTH, HEIGHT, BUTTOM_BORDER_COLOR, CANVAS)


# UM DESENHO POR BOTÃO: primeiro o ícone, depois a borda em volta
def draw_pen(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("PEN", HEIGHT)
    draw_icon(PENCIL_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_erase(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("ERASER", HEIGHT)
    draw_icon(ERASE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_bucket(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("BUCKET", HEIGHT)
    draw_icon(BUCKET_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_color_picker(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("COLOR_PICKER", HEIGHT)
    draw_icon(COLOR_PICKER_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_line_breseham(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("LINE_BRESEHAM", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_line_dda(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("LINE_DDA", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_curve(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("CURVE", HEIGHT)
    draw_icon(CURVE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_circle_hollow(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("CIRCLE_HOLLOW", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = BUTTON_SIZE // 2 - 1                                  # 6
    primitives.draw_circle_hollow(center_x, center_y, radius, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_circle_filled(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("CIRCLE_FILLED", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2
    radius = BUTTON_SIZE // 2 - 1                                  # 6
    primitives.draw_circle_filled(center_x, center_y, radius, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_rectangle_hollow(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("RECTANGLE_HOLLOW", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    primitives.draw_rectangle_hollow(x1 + 1, y1 + 1, x2 - 1, y2 - 1, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_rectangle_filled(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("RECTANGLE_FILLED", HEIGHT)
    draw_icon(BACKGROUND_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    # o draw_rectangle_filled não pinta x2/y2 (range exclui o último), então x2 e y2 do botão servem de limite
    primitives.draw_rectangle_filled(x1 + 1, y1 + 1, x2, y2, WIDTH, HEIGHT, ICON_COLOR, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_save(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("SAVE", HEIGHT)
    draw_icon(SAVE_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

def draw_new(WIDTH, HEIGHT, CANVAS):
    x1, y1, x2, y2 = get_button_rect("NEW", HEIGHT)
    draw_icon(NEW_ICON, x1, y2, WIDTH, HEIGHT, CANVAS)
    draw_button_border(x1, y1, x2, y2, WIDTH, HEIGHT, CANVAS)

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

def draw_menu(WIDTH, HEIGHT, CANVAS, COLOR_PALLETE):
    DRAW_HEIGHT = HEIGHT - get_menu_height()
    primitives.draw_rectangle_filled(0, DRAW_HEIGHT, WIDTH, HEIGHT, WIDTH, HEIGHT, BACKGROUND_COLOR, CANVAS)

    for line in MENU_STRUCTURE:
        for name in line:
            if name is None:
                continue
            if name in COLOR_PALLETE:
                draw_color_pallete_buttons(name, COLOR_PALLETE[name], WIDTH, HEIGHT, CANVAS)
            else:
                DRAW_FUNCTIONS[name](WIDTH, HEIGHT, CANVAS)

