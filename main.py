#Codigo por: Oscar Emilio Reyes Taboada A01369421
# Jose Israel Quintero Alfaro A01366861

from Tf import *
from TF_IDF import *

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

for i in range (4):
    with open("file"+str(i+1)+".txt", "w") as f:
        # The file is now empty
        pass


for i in range (4):

    print(i)
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

def menu():
    print("========================================")
    print("|        SELECCIONE UNA OPCION         |")
    print("========================================")
    print("| 1. TF                                |")
    print("| 2. TF-IDF                            |")
    print("| 3. Salir                             |")
    print("========================================")

    option = input("Que desea calcular?... ")

    if option == "1":
        tf()
        menu()
    elif option == "2":
        tf_idf()
        menu()
    elif option == "3":
        print("Gracias! 10 porfa")
    else:
        print("Por favor ingresa 1 o 2")
        menu()


menu()