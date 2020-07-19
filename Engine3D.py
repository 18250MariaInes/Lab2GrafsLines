"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR2 Lines
Main
"""

from gl import Render

#valores con los que se inicializan la ventana y viewport

width=1920
height=1080
posX = width/4
posY = height/4
#creacion de Window
#los ultimos 3 parametros es para settear el color del fondo de la ventana con parametros de 0-1 para rojo, verde y azul
r = Render(width,height,0,0,0.25)

#creacion del viewport
r.glViewPort(posX, posY, width - width/2 , height - height/2)

#cambio de color con el que se hará el punto con parametros de 0-1 para r, g, b
r.glColor(1,0,0)


r.glLine(-1,-1, 1,-1)
r.glLine(-1,-1, -1,0)
r.glLine(1,-1, 1,0)
r.glLine(-1,0, 0, 1)
r.glLine(0,1, 1,0)
r.glLine( -1, 0, 1, 0)


r.glFinish('output.bmp')



