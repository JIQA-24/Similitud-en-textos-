''' 
    A01367102 y A01366907
    Este script corre el programa de similitud de textos
    y genera los archivos de los programas en -c
    y da los vectores de frecuencia de términos
    con la técnica TF-IDF y TF

'''



def globales(prog, pos, long):
    global program
    global position
    global progLong
    program = prog
    position = pos
    progLong = long

#El script con el que se prueba será el siguiente:

from globalTypes import *
from lexer import *
from TF_IDF import *
from Tf import *

for i in range (4):
    with open("programa"+str(i+1)+".c-", "w") as f:
        # The file is now empty
        pass


for i in range (4):
    #jala los programas en -c y hace el lexer de cada uno

    #print(i)
    f = open(str('prueba'+str(i)+'.c-'), 'r')
    program = f.read() 		# lee todo el archivo a compilar
    progLong = len(program) 	# longitud original del program
    program = program + '$' 	# agregar un caracter $ que represente EOF
    position = 0 			# posición del caracter actual del string

    recibeScanner(program, position, progLong, i)
    # función para pasar los valores iniciales de las variables globales
    globales(program, position, progLong)

    token, tokenString, _ = getToken(True)
    while (token != TokenType.ENDFILE):
        token, tokenString, _ = getToken(True)
        
    f.close()

    i += 1

getTF()
getTFDIF()