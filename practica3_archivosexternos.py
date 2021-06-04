
import io

class Archivo:

    def __init__(self,nombre,permiso):
        self.nombre = nombre
        self.permiso = permiso
    

    def crearArchivo(self):

        self.archivo = open(self.nombre,self.permiso)
        self.archivo.write("Hola Mundo")
        self.archivo.seek(0)
        print(self.archivo.read())
    


nuevoArchivo = Archivo("agregar.txt","r+")
nuevoArchivo.crearArchivo()