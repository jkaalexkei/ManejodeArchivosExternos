
import io


class ArchivoExterno:

    def __init__(self,nombrearchivo,texto,permisow,persmisor):
        self.texto = texto
        self.permisow = permisow
        self.permisor = persmisor
        self.nombrearchivo = nombrearchivo

    def creararchivo(self):
        self.archivo = open(self.nombrearchivo,self.permisow)
        self.archivo.write(self.texto)
        self.archivo.close()

    def leerarchivo(self):
        self.archivo = open(self.nombrearchivo,self.permisor)
        self.contenido = self.archivo.read()
        print("El texto del archivo es: \n",self.contenido)
        
    
    def agregarInformacion(self):
        self.archivo = open(self.nombrearchivo,"a")

        if len(self.contenido) > 0:
            self.archivo.write("Informacion adiciona")
        else:
            print("otra situacion")
    
    


        


textodelarchivo = input("Ingrese el texto para el archivo:\n")
nuevoarchivo = ArchivoExterno("textodeprueba.txt","textodelarchivo","w","r")

nuevoarchivo.creararchivo()
nuevoarchivo.leerarchivo()
nuevoarchivo.agregarInformacion()


    
    






