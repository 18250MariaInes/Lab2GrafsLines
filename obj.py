#Carga de archivo OBJ

class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines=file.read().splitlines()
        
        self.vertices=[]
        self.normals=[]
        self.texcoords=[]
        self.faces=[]

        
        self.read()

        #print(self.vertices)
        """for face in self.faces:
            print(face)"""
        #print("-----------------------------------------------------------------------")

    def read(self):
        for line in self.lines:
            #print(line.split(' ',1))
            if line:
                prefix,value=line.split(' ',1)
                if prefix == 'v': # vertices
                    self.vertices.append(list(map(float,value.split(' '))))
                elif prefix == 'vn': #normales
                    self.normals.append(list(map(float,value.split(' '))))
                elif prefix == 'vt': #textcoords
                    self.texcoords.append(list(map(float,value.split(' '))))
                elif prefix == 'f': #faces
                    self.faces.append([list(map(int,vert.split('/'))) for vert in value.split(' ')])




        

