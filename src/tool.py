import math
import numpy as np
import struct
import zlib
from tkinter import Tk, filedialog

import primitives
import mouse

def pencil(x, y, pressed, last_point, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    if not pressed:
        return None

    if last_point is None:
        primitives.stamp(x, y, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    else:
        primitives.draw_bresenham_line(last_point[0], last_point[1], x, y, WIDTH, HEIGHT, COLOR, CANVAS, MASK)

    return (x, y)

def erase(x, y, pressed, last_point, WIDTH, HEIGHT, CANVAS, MASK=[[1]]):
    return pencil(x, y, pressed, last_point, WIDTH, HEIGHT, [255,255,255], CANVAS, MASK)


def line(start, end, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    primitives.draw_bresenham_line(start[0], start[1], end[0], end[1], WIDTH, HEIGHT, COLOR, CANVAS, MASK)

def get_corners(start, end):
    x1, x2 = sorted((start[0], end[0]))
    y1, y2 = sorted((start[1], end[1]))
    return x1, y1, x2, y2

def rectangle_hollow(start, end, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    x1, y1, x2, y2 = get_corners(start, end)
    primitives.draw_rectangle_hollow(x1, y1, x2, y2, WIDTH, HEIGHT, COLOR, CANVAS, MASK)

def rectangle_filled(start, end, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    x1, y1, x2, y2 = get_corners(start, end)
    primitives.draw_rectangle_filled(x1, y1, x2 + 1, y2 + 1, WIDTH, HEIGHT, COLOR, CANVAS)

def get_radius(center, edge):
    return int(round(math.hypot(edge[0] - center[0], edge[1] - center[1])))

def circle_hollow(center, edge, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    primitives.draw_circle_hollow(center[0], center[1], get_radius(center, edge), WIDTH, HEIGHT, COLOR, CANVAS, MASK)

def circle_filled(center, edge, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    primitives.draw_circle_filled(center[0], center[1], get_radius(center, edge), WIDTH, HEIGHT, COLOR, CANVAS)

SHAPES = {
    "LINE_BRESEHAM":    line,
    "RECTANGLE_HOLLOW": rectangle_hollow,
    "RECTANGLE_FILLED": rectangle_filled,
    "CIRCLE_HOLLOW":    circle_hollow,
    "CIRCLE_FILLED":    circle_filled,
}

def draw_shape(name, start, end, preview, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    if preview and name == "RECTANGLE_FILLED":
        name = "RECTANGLE_HOLLOW"
        MASK = [[1]]
    if preview and name == "CIRCLE_FILLED":
        name = "CIRCLE_HOLLOW"
        MASK = [[1]]
    SHAPES[name](start, end, WIDTH, HEIGHT, COLOR, CANVAS, MASK)


# FERRAMENTAS DE UM CLIQUE
def bucket(x, y, WIDTH, HEIGHT, COLOR, CANVAS):
    if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
        return
    if np.array_equal(primitives.get_pixel(x, y, WIDTH, HEIGHT, CANVAS), COLOR):
        return                                  # já está dessa cor, nada a pintar
    primitives.flood_fill_bucket_neighbor_4(x, y, WIDTH, HEIGHT, COLOR, CANVAS)

def color_picker(x, y, WIDTH, HEIGHT, CANVAS):
    return [int(c) for c in primitives.get_pixel(x, y, WIDTH, HEIGHT, CANVAS)]

def new(WIDTH, HEIGHT, CANVAS):
    CANVAS[:HEIGHT, :WIDTH] = 255

def ask_save_path():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    path = filedialog.asksaveasfilename(
        title="Salvar desenho",
        defaultextension=".png",
        filetypes=[("Imagem PNG", "*.png")],
        initialfile="desenho.png",
    )
    root.destroy()
    return path

def save(WIDTH, HEIGHT, CANVAS, filename="desenho.png"):
    image = CANVAS[:HEIGHT, :WIDTH][::-1]
    raw = b"".join(b"\x00" + row.tobytes() for row in image)

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))

    header = struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0)

    with open(filename, "wb") as file:
        file.write(b"\x89PNG\r\n\x1a\n")
        file.write(chunk(b"IHDR", header))
        file.write(chunk(b"IDAT", zlib.compress(raw)))
        file.write(chunk(b"IEND", b""))