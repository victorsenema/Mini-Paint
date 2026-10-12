import glfw             
from OpenGL.GL import *
import numpy as np

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
    
def render():
     lin = dda_line(10,10,100,100)


def dda_line( x0, y0, x1, y1):
        points = []

        # Calcula diferenças
        dx = x1 - x0
        dy = y1 - y0

        # Calcula o número de passos necessário
        # O passo será o maior valor absoluto entre dx e dy
        steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

        # Se a linha é um ponto único
        if steps == 0:
            return [(int(x0), int(y0))]

        # Calcula incrementos
        x_increment = dx / steps
        y_increment = dy / steps

        # Ponto inicial
        x = x0
        y = y0

        # Gera os pontos
        for i in range(int(steps) + 1):
            points.append((int(round(x)), int(round(y))))
            x += x_increment
            y += y_increment

        return points

def create_window(width, height):
    glfw.init()
    window = glfw.create_window( width, height, "Mini Paint", None, None )
    glfw.make_context_current(window)

    return window

def update(window):
     while not glfw.window_should_close( window ):
            glfw.poll_events()
     
            render()
            # Change Buffers FrontBuffer (Screen Buffer), BackBuffer (GPU Buffer)
            glfw.swap_buffers( window )
        
if __name__ == "__main__":
    window = create_window(500,600)
    update(window)