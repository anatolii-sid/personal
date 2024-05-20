import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import random
import math
import pywavefront
import ctypes
from data import hidden_stuff


scene = pywavefront.Wavefront(hidden_stuff.file_path, collect_faces=True)

scene_box = (scene.vertices[0], scene.vertices[0])
for vertex in scene.vertices:
    min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
    scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]


def model():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)

    for mesh in scene.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*scene.vertices[vertex_i])
        glEnd()

    glPopMatrix()


pygame.font.init()
font = pygame.font.SysFont('Times New Roman', 64)


def drawText(x, y, text):
    textSurface = font.render(text, True, (255, 77, 77, 150)).convert_alpha()
    textData = pygame.image.tostring(textSurface, "RGBA", True)
    glWindowPos2d(x, y)
    glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


def main():
    pygame.init()
    pygame.display.set_caption('This was pretty fun to learn')
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    gluPerspective(45, display[0]/display[1], 0.1, 40.0)

    glTranslatef(0.0, -1.5, -10)

    glRotatef(45, 45, 45, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # point_cube()
        # point_sphere()

        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        model()
        drawText(50, 500, hidden_stuff.text)
        # draw_buffer(buffer_obj, no_points)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        pygame.display.flip()
        pygame.time.wait(10)


main()

