from collections import deque
import numpy as np

# Stamp it's to use the brush size
def stamp(x, y, MASK, WIDTH, HEIGHT, COLOR, CANVAS):
    center = len(MASK) // 2
    for i in range(len(MASK)):
        for j in range(len(MASK[0])):
            if MASK[i][j] == 1:
                set_pixel_color(x + j - center, y + i - center, WIDTH, HEIGHT, COLOR, CANVAS)

def set_pixel_color(x, y, WIDTH, HEIGHT, COLOR, CANVAS):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        CANVAS[y,x] = COLOR

def get_pixel(x, y, WIDTH, HEIGHT, CANVAS):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        return CANVAS[y, x].copy()
    else:
        return [255,255,255]

def draw_bresenham_line(x1, y1, x2, y2, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    step_x = 1 if x2 > x1 else -1
    step_y = 1 if y2 > y1 else -1

    x = x1
    y = y1

    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            stamp(x, y, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
            if p >= 0:
                y += step_y
                p -= 2 * dx
            p += 2 * dy
            x += step_x
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            stamp(x, y, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
            if p >= 0:
                x += step_x
                p -= 2 * dy
            p += 2 * dx
            y += step_y

def dda():
    return 1

def bezier_point(p1, p2, p3, p4, t):
    u = 1 - t
    b1 = u * u * u
    b2 = 3 * t * u * u
    b3 = 3 * t * t * u
    b4 = t * t * t
    x = b1 * p1[0] + b2 * p2[0] + b3 * p3[0] + b4 * p4[0]
    y = b1 * p1[1] + b2 * p2[1] + b3 * p3[1] + b4 * p4[1]
    return int(round(x)), int(round(y))

def distance(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5

def draw_bezier_curve(p1, p2, p3, p4, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    length = distance(p1, p2) + distance(p2, p3) + distance(p3, p4)
    steps = max(1, int(length / 2))

    previous = p1
    for i in range(1, steps + 1):
        current = bezier_point(p1, p2, p3, p4, i / steps)
        draw_bresenham_line(previous[0], previous[1], current[0], current[1], WIDTH, HEIGHT, COLOR, CANVAS, MASK)
        previous = current


def draw_rectangle_hollow(x1, y1, x2, y2, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    for x in range(x1,x2+1):
        stamp(x, y1, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
        stamp(x, y2, MASK, WIDTH, HEIGHT, COLOR, CANVAS)

    for y in range(y1,y2+1):
        stamp(x1, y, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
        stamp(x2, y, MASK, WIDTH, HEIGHT, COLOR, CANVAS)

def draw_rectangle_filled(x1, y1, x2, y2, WIDTH, HEIGHT, COLOR, CANVAS):
    for x in range(x1,x2):
        for y in range(y1,y2):
            set_pixel_color(x, y, WIDTH, HEIGHT, COLOR, CANVAS)

def draw_simetric_points(x, y, x_displacement, y_displacement, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    stamp(x + x_displacement, y + y_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x - x_displacement, y + y_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x + x_displacement, y - y_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x - x_displacement, y - y_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x + y_displacement, y + x_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x - y_displacement, y + x_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x + y_displacement, y - x_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)
    stamp(x - y_displacement, y - x_displacement, MASK, WIDTH, HEIGHT, COLOR, CANVAS)

def draw_circle_hollow(x, y, r, WIDTH, HEIGHT, COLOR, CANVAS, MASK=[[1]]):
    x_displacement = 0
    y_displacement = r
    p_decision = 1 - r

    draw_simetric_points(x, y, x_displacement, y_displacement, WIDTH, HEIGHT, COLOR, CANVAS, MASK)

    while y_displacement > x_displacement:
        x_displacement += 1

        if p_decision < 0:
            p_decision += (2 * x_displacement) + 1
        else:
            y_displacement -= 1
            p_decision += 2 * (x_displacement - y_displacement) + 1

        draw_simetric_points(x, y, x_displacement, y_displacement, WIDTH, HEIGHT, COLOR, CANVAS, MASK)

def draw_circle_filled(x, y, r, WIDTH, HEIGHT, COLOR, CANVAS):
    x_displacement = 0
    y_displacement = r
    m_decision = 5 - (4 * r)

    while x_displacement <= y_displacement:
        draw_bresenham_line(x - x_displacement, y - y_displacement, x + x_displacement, y - y_displacement, WIDTH, HEIGHT, COLOR, CANVAS)
        draw_bresenham_line(x - x_displacement, y + y_displacement, x + x_displacement, y + y_displacement, WIDTH, HEIGHT, COLOR, CANVAS)
        draw_bresenham_line(x - y_displacement, y - x_displacement, x + y_displacement, y - x_displacement, WIDTH, HEIGHT, COLOR, CANVAS)
        draw_bresenham_line(x - y_displacement, y + x_displacement, x + y_displacement, y + x_displacement, WIDTH, HEIGHT, COLOR, CANVAS)

        if m_decision > 0:
            y_displacement -= 1
            m_decision -= 8 * y_displacement

        x_displacement = x_displacement + 1
        m_decision = m_decision + (8 * x_displacement) + 4


def get_neighbors_8(x, y, target_color, WIDTH, HEIGHT, CANVAS):
    neighbors_8 = []
    i = 0

    for x_i in range(-1,2):
        for y_j in range (-1,2):
            if x_i != 0 or y_j != 0:
                new_x = x + x_i
                new_y = y + y_j

                if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and np.array_equal(CANVAS[new_y, new_x], target_color):
                    neighbors_8.append([new_x, new_y])
    
    return neighbors_8

def get_neighbors_4(x, y, target_color, WIDTH, HEIGHT, CANVAS):
    neighbors_4 = []

    directions = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and np.array_equal(CANVAS[new_y, new_x], target_color):
            neighbors_4.append((new_x, new_y))

    return neighbors_4

def flood_fill_bucket_neighbor_8(start_x, start_y, WIDTH, HEIGHT, COLOR, CANVAS):
    queue = deque()
    visited = set()

    target_color = get_pixel(start_x, start_y, WIDTH, HEIGHT, CANVAS)

    queue.append([start_x, start_y])
    visited.add((start_x, start_y))

    while queue:
        current_x, current_y = queue.popleft()
        set_pixel_color(current_x, current_y, WIDTH, HEIGHT, COLOR, CANVAS)
        neighbors = get_neighbors_8( current_x, current_y, target_color, WIDTH, HEIGHT, CANVAS)

        for neighbor in neighbors:
            neighbor = tuple(neighbor)

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

# def flood_fill_bucket_neighbor_4(start_x, start_y, WIDTH, HEIGHT, COLOR, CANVAS):
#     queue = deque()
#     visited = set()

#     target_color = get_pixel(start_x, start_y, WIDTH, HEIGHT, CANVAS)

#     same_color = np.all(CANVAS[:HEIGHT, :WIDTH] == target_color, axis=2).tolist()

#     queue.append((start_x, start_y))
#     visited.add((start_x, start_y))

#     directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

#     while queue:
#         current_x, current_y = queue.popleft()

#         for dx, dy in directions:
#             new_x = current_x + dx
#             new_y = current_y + dy
#             neighbor = (new_x, new_y)

#             if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and same_color[new_y][new_x] and neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

#     xs, ys = zip(*visited)
#     CANVAS[list(ys), list(xs)] = COLOR

#     return visited

def get_neighbors_4(x, y, target_color, WIDTH, HEIGHT, CANVAS):
    neighbors_4 = []

    directions = [
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    ]

    for dx, dy in directions:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and np.array_equal(CANVAS[new_y, new_x], target_color):
            neighbors_4.append((new_x, new_y))

    return neighbors_4


#NOT OTPTIMZED BUCKET N 4
def flood_fill_bucket_neighbor_4(start_x, start_y, WIDTH, HEIGHT, COLOR, CANVAS):
    queue = deque()
    visited = set()

    target_color = get_pixel(start_x, start_y, WIDTH, HEIGHT, CANVAS)

    queue.append([start_x, start_y])
    visited.add((start_x, start_y))

    while queue:
        current_x, current_y = queue.popleft()
        set_pixel_color(current_x, current_y, WIDTH, HEIGHT, COLOR, CANVAS)
        neighbors = get_neighbors_4( current_x, current_y, target_color, WIDTH, HEIGHT, CANVAS)

        for neighbor in neighbors:
            neighbor = tuple(neighbor)

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited