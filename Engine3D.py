"""
Maria Ines Vasquez Figueroa
18250
Gráficas
Lab 1 Filling Polygons
Main
"""

from gl import Render


#valores con los que se inicializan la ventana y viewport

width=1000
height=500

#creacion de Window

r = Render(width,height)
r.glClearColor(0, 0, 0) #este es background color
r.glClear()
r.glColor(1, 0, 0)

#poly 1
poly1 = [(165, 380), (185, 360), 
(185, 360), (180, 330),
(180, 330), (207, 345),
(207, 345), (233, 330), 
(233, 330), (230, 360),
(230, 360), (250, 380),
(250, 380), (220, 385),
(220, 385), (205, 410),
(205, 410), (193, 383),
(193, 383), (165, 380)]
r.drawPoly(poly1)
r.filling_polygon(poly1)
r.glColor(0, 1, 0)

#poly 2
poly2 = [(321, 335), (288, 286),
(288, 286), (339, 251),
(339, 251), (374, 302),
(374, 302), (321, 335)]
r.drawPoly(poly2)
r.filling_polygon(poly2)
r.glColor(0, 0, 1)

#poly 3
poly3 = [(377, 249), (411, 197),
(411, 197), (436, 249),
(436, 249), (377, 249)]
r.drawPoly(poly3)
r.filling_polygon(poly3)
r.glColor(1, 0, 1)

#poly 4
poly4 = [(413, 177), (448, 159),
(448, 159), (502, 88),
(502, 88), (553, 53),
(553, 53), (535, 36),
(535, 36), (676, 37),
(676, 37), (660, 52),
(660, 52), (750, 145),
(750, 145), (761, 179),
(761, 179), (672, 192),
(672, 192), (659, 214),
(659, 214), (615, 214),
(615, 214), (632, 230),
(632, 230), (580, 230),
(580, 230), (597, 215),
(597, 215), (552, 214),
(552, 214), (517, 144),
(517, 144), (466, 180),
(413, 177), (466, 180)]
r.drawPoly(poly4)
r.filling_polygon(poly4)
r.glColor(0, 1, 1)

#poly 5
poly5 = [(682, 175), (708, 120),
(708, 120), (735, 148),
(735, 148), (739, 170),
(739, 170), (682, 175)]
r.drawPoly(poly5)
r.filling_polygon(poly5)





r.glFinish('output.bmp')





