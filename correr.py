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

f = open('prueba2.c-', 'r')
program = f.read() 		# lee todo el archivo a compilar
progLong = len(program) 	# longitud original del program
program = program + '$' 	# agregar un caracter $ que represente EOF
position = 0 			# posición del caracter actual del string

recibeScanner(program, position, progLong)
# función para pasar los valores iniciales de las variables globales
globales(program, position, progLong)

token, tokenString, _ = getToken(True)
while (token != TokenType.ENDFILE):
    token, tokenString, _ = getToken(True)
    
file1.close()