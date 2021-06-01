
#TRABAJAR CON FICHEROS O ARCHIVOS EXTERNOS DE TEXTO CON EL MODULO IO

# PUNTEROS EN TEXTO: 

from io import open 

#   archivo_texto = open("archivo.txt","r")
#archivo_texto.write("\n Esta es una linea adicional agregada")
#archivo_texto.seek(11)#posiciona el punturo donde se indique
#print(archivo_texto.read(11))#hace una lectura hasta donde se le indique  
#   archivo_texto.seek(len(archivo_texto.read())/2)#Esto ubiica  el puntero en la mitad del texto que haya y a partir de alli hace  la lectura del texto

#  print(archivo_texto.read())
#POSICIONAMIENTO DEL CURSOR METODO SEEK Y RECIBE UN PARAMENTRO QUE ES EL NUMERO DE CARACTER DONDE SE QUERE UBICAR EL CURSOR

#ABRIR UN ARCHIVO EN MODO LECTURA Y ESCRITURA

archivo_texto = open("archivo.txt","r+") #de esta manera se abre el archivo en modo lectura y escritura

archivo_texto.write("comienzo del texto")#agrega un linea al principio del texto reemplazando la existente

lista_texto = archivo_texto.readlines()#agregamos el numero de lineas que tiene el texto a la variable

lista_texto[1] = "esta linea ha sido inicluida desde el exterior\n" #en la linea especificada agregamos una linea adiciional

archivo_texto.seek(0)#posicionamos el puntero en la primera linea

archivo_texto.writelines(lista_texto)#este metodo writelines pide por parametro un lista





archivo_texto.close()

