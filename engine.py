#Programa principal
import random
from shaders import *
from gl import *
from obj import *
from texture import *
width = 1080  #alto de la pantalla
height = 1920 #ancho de la pantalla
rende = Renderer(height,width)

rende.active_shader = toon
rende.active_texture = Texture("earthDay.bmp")
rende.glLoadModel("models/MouseS.obj",translate=V3(0,0,-5),rotate=V3(0,0,0),scale=V3(1,1,1))

rende.active_shader = thermal
rende.active_texture = Texture("earthDay.bmp")
rende.glLoadModel("models/MouseS.obj",translate=V3(3,0,-5),rotate=V3(0,0,0),scale=V3(1,1,1))

rende.active_shader = nightVision
rende.active_texture = Texture("earthDay.bmp")
rende.glLoadModel("models/MouseS.obj",translate=V3(-5,0,-10),rotate=V3(0,0,0),scale=V3(1,1,1))

rende.active_shader = negative
rende.active_texture = Texture("earthDay.bmp")
rende.glLoadModel("models/MouseS.obj",translate=V3(0,-2.5,-10),rotate=V3(0,0,0),scale=V3(1,1,1))

rende.active_shader = aura
rende.active_texture = Texture("earthDay.bmp")
rende.glLoadModel("models/MouseS.obj",translate=V3(0,3,-10),rotate=V3(0,0,0),scale=V3(1,1,1))





rende.glFinish("./salida.bmp")