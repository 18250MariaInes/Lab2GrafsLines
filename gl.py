"""
Maria Ines Vasquez Figueroa
18250
Gráficas
SR2 Lines 
Funciones
"""
import struct

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h',w)

def dword(d):
    # 4 bytes
    return struct.pack('=l',d)

def color(r, g, b):
    return bytes([b, g, r])


BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Render(object):
    def __init__(self, width, height, red, green, blue):
        self.glInit(width, height, red, green, blue)

    #Inicializa objetos internos
    def glInit(self, width, height, red, green, blue):
        #esto se establece ahora en la funcion glCreatWindow
        """self.width = width
        self.height = height"""
        self.glCreateWindow(width, height)
        self.curr_color = WHITE
        self.curr_color_bg=BLACK
        self.glClearColor(red, green, blue)
        self.glClear()

    #inicializa framebuffer
    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    #define area de dibujo
    def glViewPort(self, x, y, width, height):
        self.vportwidth = width
        self.vportheight = height
        self.vportx = x
        self.vporty = y

    #cambia el color con el que se llena el mapa de bits (fondo)
    def glClearColor(self, red, green, blue):
        nred=int(255*red)
        ngreen=int(255*green)
        nblue=int(255*blue)
        self.curr_color_bg = color(nred, ngreen, nblue)

    #llena el mapa de bits de un solo color predeterminado antes
    def glClear(self):
        self.pixels = [ [ self.curr_color_bg for x in range(self.width)] for y in range(self.height) ]
    
    #dibuja el punto en relación al viewport
    def glVertex(self, x, y):
        nx=int((x+1)*(self.vportwidth/2)+self.vportx)
        ny=int((y+1)*(self.vportheight/2)+self.vporty)
        self.pixels[ny][nx] = self.curr_color
    
    #cambia de color con el que se hará el punto con parametros de 0-1
    def glColor(self, red, green, blue):
        nred=int(255*red)
        ngreen=int(255*green)
        nblue=int(255*blue)
        self.curr_color = color(nred, ngreen, nblue)
    
    def glVertex_coord(self, x,y):#helper para dibujar puntas en la funcion de glLine
        self.pixels[y][x]=self.curr_color

    #escribe el archivo de dibujo
    def glFinish(self, filename):
        archivo = open(filename, 'wb')

        # File header 14 bytes
        #f.write(char('B'))
        #f.write(char('M'))

        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))

        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # Image Header 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))

        # Pixeles, 3 bytes cada uno

        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])


        archivo.close()

    def glLine(self, x0, y0, x1, y1): #algoritmo de clase modificado en base al algoritmo de Bersenham extraido de : https://www.geeksforgeeks.org/bresenhams-line-generation-algorithm/
        x0 = int(( x0 + 1) * (self.vportwidth / 2 ) + self.vportx)
        x1 = int(( x1 + 1) * (self.vportwidth / 2 ) + self.vportx)
        y0 = int(( y0 + 1) * (self.vportheight / 2 ) + self.vporty)
        y1 = int(( y1 + 1) * (self.vportheight / 2 ) + self.vporty)

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        inc = dy > dx

        if inc:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        limit = 0.5
    
        #a diferencia del visto en clase, el algoritmo consultado inicializa m como 2 veces el diferencial en y 
        #y offset como la resta entre la pendiente m y 2 veces el diferencial en x
        m=2*(dy)
        offset=m-2*dx
        y = y0
        for x in range(x0, x1 + 1):
            if inc:
                self.glVertex_coord(y, x)
            else:
                self.glVertex_coord(x, y)
            offset += m
            if offset >= limit:
                if y0 < y1:
                    y += 1
                else:
                    y-=1
                limit += 1
                #igualmente cuando offset es mayor o igual que el limite 0.5, se le resta 2 veces el diferencial en x
                offset-=2*dx
    
    def glLine_c(self, x0, y0, x1, y1):#algoritmo realizado con Carlos en clase, lo mantengo como comparacion y el resultado es muy similar al desarrollado por mi
        x0 = int(( x0 + 1) * (self.vportwidth / 2 ) + self.vportx)
        x1 = int(( x1 + 1) * (self.vportwidth / 2 ) + self.vportx)
        y0 = int(( y0 + 1) * (self.vportheight / 2 ) + self.vporty)
        y1 = int(( y1 + 1) * (self.vportheight / 2 ) + self.vporty)

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        inc = dy > dx

        if inc:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)

        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0
        for x in range(x0, x1 + 1):
            if inc:
                self.glVertex_coord(y, x)
            else:
                self.glVertex_coord(x, y)
            offset += m
            if offset >= limit:
                y += 1 if y0 < y1 else -1
                limit += 1



                











