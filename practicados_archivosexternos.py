
import io

texto1 = open("documento.txt","w")

contenido ="esto es una prueba de infomacion"

textofinal = texto1.write(contenido)

texto1.close()

texto2 = open("documento.txt","r")
print(texto2.read())