import glfw
from OpenGL.GL import *
import numpy as np

import canva_manipulation

# 1- Pixel on the Screen:
    # Change Buffers FrontBuffer (Screen Buffer), BackBuffer (GPU Buffer)
    # glfw.swap_buffers( window )

    # The Back Buffer stores what as draw 2 frames ago
    # if we not clean the buffer it will appear trash
    # glClear(GL_COLOR_BUFFER_BIT) 

# 2- GLFW: window, context and events
    # glfw.init() -> initalize the library (return false if it fails)
    # glfw.create_window(width, height, Title, None, None)
    # glfw.make_context_current(window)  -> Draw on this window (without that all the gl* calls don't work)
    # glfw.poll_events() -> process the pending events
    # glfw.wait_events() -> sleeps till an event happens
    # glfw.window_should_close(window) -> user close window ('X' button)
    # glfw.terminate() -> free the resources at the end

# 3- NDC: Normalized Device Coordinates (x,y [-1,1])
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glOrtho(0, width, heigth, 0, -1, 1)  # left, right, bottom, top, near, far
    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()

HEIGHT, WIDTH = 600, 500
SELECTED_COLOR = [0,0,0]
CANVAS = np.full((HEIGHT, WIDTH, 3), 255, dtype=np.uint8)

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

def update(window):

    # Update loop
    while not glfw.window_should_close(window):
        # Render
        glClear(GL_COLOR_BUFFER_BIT)

        # Using a Canvas, it's like a third buffer that we use to store every pixel
        # the user drew on the window

        # canva_manipulation.draw_bresenham_line(10,10, 200,30, WIDTH, HEIGHT, SELECTED_COLOR, CANVAS)
        # canva_manipulation.draw_rectangle_hollow(20,20, 100,200, WIDTH, HEIGHT, SELECTED_COLOR, CANVAS)
        # canva_manipulation.draw_rectangle_filled(300,0, 400,50, WIDTH, HEIGHT, SELECTED_COLOR, CANVAS)
        canva_manipulation.draw_circle_hollow(250,250, 20, WIDTH, HEIGHT, SELECTED_COLOR, CANVAS)
        canva_manipulation.draw_circle_filled(400,400, 50, WIDTH, HEIGHT, SELECTED_COLOR, CANVAS)
        glRasterPos2f(-1, -1)
        glDrawPixels(WIDTH, HEIGHT, GL_RGB, GL_UNSIGNED_BYTE, CANVAS)
        # Swap
        glfw.swap_buffers(window)

        # Process Events Pool
        glfw.poll_events()

    glfw.terminate()
    return
        
        
if __name__ == "__main__":
    window = create_window(WIDTH, HEIGHT)
    update(window)