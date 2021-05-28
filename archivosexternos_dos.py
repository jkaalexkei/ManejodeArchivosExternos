from io import open #uso del modulo io y el metodo open

#abrir archivo en modo escritura
#    archivo_texto = open("archivo.txt","w")#recibe dos argumentos (nombrearchivo,modoenelquesevaabrir)se puede abrir en modo lectura,escritura, append para agregar iniformacion a un archivo existente

#maneras de trabajar con un archivo externo mediante el uso del metodo open en su segundo argumento:

# "w" --> escribir en un archivo
# "r" --> modo solo lectura
# "a" --> modo append para agregar informacion

frase = "Practicando agregar informacion a un archivo externo"
#    archivo_texto = open("archivo.txt","w")
#    archivo_texto.write(frase)#aca agregamos informacion al archivo mediante el metodo write el cual recibe un argumento que es el texto que se quiere agregar

#abrir archivo en modo lectura

#archivo_texto = open("archivo.txt","r")#aca se le pasa  como argumento el nombre del archivo y el modo 
#   texto =archivo_texto.read()#aca leemos la informacion proveniente del archivo externo
#print(texto)

#   lineas_texto = archivo_texto.readlines()#-->muestra las lineas del texto en una lista
#    print(lineas_texto)#--> aca se muestra las lineas que tenga el archivo en una lista
#    print(lineas_texto[1])#--> de esta manera accedemos a una linea o elemento en especifico del texto que haya en el archivo externo

#metodo  readlines() = permite leer un archivo line a linea y almacenar la informacion en una lista

archivo_texto = open("archivo.txt","a")#aca abrimos el archivo en modo para agregar informacion adicional
archivo_texto.write("\n Esta es una linea adicional agregada")

archivo_texto.close()#cerramos el archivo que hemos abierto

