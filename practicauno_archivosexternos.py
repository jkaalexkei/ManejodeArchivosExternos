
from typing import IO


class ArchivoExterno:

    def __init__(self,texto):

        self.miTexto = texto

    def CrearArchivoExt(self,nombrearchivo,permiso):

        self.archivoext = open(nombrearchivo,permiso)
    
    def AgregarTextoArchExt(self):

        self.archivoext.write(self.miTexto)
        print("La informacion se agrego correctamente..!")
        self.archivoext.close()

    def leerInfoArchExte(self,nombredoc,permisodoc):

        self.archivoext = open(nombredoc,permisodoc)
        infoarchext = self.archivoext.read()
        print(infoarchext)
        self.archivoext.close()
    


nuevoarchivoext = ArchivoExterno("Hola mundo esto esta dentro del archivo externo documento y ademas usando la programacion orientada a objetos")

nuevoarchivoext.CrearArchivoExt("documento2.doc","w")
nuevoarchivoext.AgregarTextoArchExt()

otroarchivo = input("ingrese el nombre del archivo con su extension: ")
nuevoarchivoext.leerInfoArchExte(otroarchivo,"r")




        

