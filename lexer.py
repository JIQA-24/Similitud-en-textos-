'''
Este es un código que implementa un analizador léxico para c-.
La función recibeScanner se utiliza para inicializar las variables globales program,
position y programLength con los valores que se pasan como argumentos.
La función reservedLookup busca en la lista de palabras reservadas una coincidencia 
con una cadena de caracteres que se pasa como argumento. 
Si se encuentra una coincidencia, se devuelve el valor correspondiente de TokenType. 
Si no se encuentra una coincidencia, se devuelve TokenType.ID.

Mientras que state no sea StateType.DONE, el programa lee el carácter 
actual de program[position] y lo guarda en c.
En general, la función getToken devuelve el tipo de token actual (currentToken) y la cadena 
de caracteres leída hasta ahora (tokenString). 
Si imprime es True, también imprime el tipo  de token y la cadena de caracteres en la consola.
'''


from globalTypes import *

lineno = 1

def recibeScanner(prog, pos, long): # función para pasar los valores iniciales de las variables globales
    global program
    global position
    global programLength
    program = prog
    position = pos
    programLength = long

def reservedLookup(tokenString): # busca en la lista de palabras reservadas
    for w in ReservedWords:
        if tokenString == w.value:
            return TokenType(tokenString)
    return TokenType.ID

def getToken(imprime = True): # función principal
    global position, lineno # variables globales
    tokenString = "" # string for storing token
    currentToken = None # is a TokenType value
    state = StateType.START # current state - always begins at START
    save = True # flag to indicate save to tokenString
    while (state != StateType.DONE): # loop until state is DONE
        c = program[position]
        save = True
        if state == StateType.START:
            if c.isdigit():
                state = StateType.INNUM
            elif c.isalpha():
                state = StateType.INID
            elif ((c == ' ') or (c == '\t') or (c == '\n')):
                save = False
                if (c == '\n'):
                    #print("línea: ", lineno)
                    lineno += 1 # incrementa el número de línea
            elif c == '/*':
                save = False
                state = StateType.INCOMMENT
            else:
                state = StateType.DONE
                if position == programLength: #EOF
                    save = False
                    currentToken = TokenType.ENDFILE
                elif c == '=':
                    cc = program[position+1]
                    if cc =='=':
                        currentToken = TokenType.IS
                        position += 1
                        c='=='
                    else:
                        currentToken = TokenType.EQ
                elif c == '<':
                    cc = program[position+1]
                    if cc =='=':
                        currentToken = TokenType.LE
                        position += 1
                        c='<='
                    else:
                        currentToken = TokenType.LT
                elif c == '>':
                    cc= program[position+1]
                    if cc =='=':
                        currentToken = TokenType.GE
                        position += 1
                        c='>='
                    else:
                        curretToken = TokenType.GT
                elif c == '+':
                    currentToken = TokenType.PLUS
                elif c == '-':
                    currentToken = TokenType.MINUS
                elif c == '*':
                    currentToken = TokenType.TIMES
                elif c == '/':
                    cc = program[position+1]
                    if cc =='*':
                        save = False
                        state = StateType.INCOMMENT
                    else:
                        currentToken = TokenType.OVER
                elif c == '(':
                    currentToken = TokenType.LPAREN
                elif c == ')':
                    currentToken = TokenType.RPAREN
                elif c == ';':
                    currentToken = TokenType.SEMI
                elif c == ',':
                    currentToken = TokenType.COMA
                elif c == '[':
                    currentToken = TokenType.LBOX
                elif c == ']':
                    currentToken = TokenType.RBOX
                elif c == '{':
                    currentToken = TokenType.LKEY
                elif c == '}':
                    currentToken = TokenType.RKEY
                elif c == '!':
                    cc = program[position+1]
                    if cc =='=':
                        currentToken = TokenType.NE
                        position += 1
                        c='!='
                    else:
                        currentToken = TokenType.ERROR
                        print("ERROR in: ", program[position], "line: ", lineno)
                else:
                    currentToken = TokenType.ERROR
                    print("ERROR in: ", program[position], "line: ", lineno)
        elif state == StateType.INCOMMENT: # comentario
            save = False
            if position == programLength: #EOF
                state = StateType.DONE
                currentToken = TokenType.ENDFILE
            elif c == '*' and program[position+1] == '/':
                position += 1
                state = StateType.START
            elif c == '\n':
                #print("línea: ", lineno)
                lineno += 1
        elif state == StateType.INASSIGN: # asignación
            state = StateType.DONE
            if c == '=':
                currentToken = TokenType.ASSIGN
            else:
                # backup in the input
                if position <= programLength:
                    position -= 1 # ungetNextChar()
                save = False
                currentToken = TokenType.ERROR
                print("ERROR in: ", program[position], "line: ", lineno)
                
        elif state == StateType.INNUM: # número
            if not c.isdigit():
                if c.isalpha():
                    print("ERROR in: ", program[position], "line: ", lineno)
                # backup in the input
                if position <= programLength:
                    position -= 1 # ungetNextChar()
                save = False
                state = StateType.DONE
                currentToken = TokenType.NUM
            
        elif state == StateType.INID: # identificador
            if not c.isalpha():
                if c.isdigit():
                    print("ERROR in: ", program[position], "line: ", lineno)
                # backup in the input
                if position <= programLength:
                    position -= 1 # ungetNextChar()
                save = False
                state = StateType.DONE
                currentToken = TokenType.ID
        elif state == StateType.DONE: # final
            None
        else: # should never happen
            print('Scanner Bug: state= '+str(state))
            state = StateType.DONE
            currentToken = TokenType.ERROR
            raise StateType(f"Unrecognized token: {currentToken}")

        if save:
            tokenString = tokenString + c
        if state == StateType.DONE:
            if currentToken == TokenType.ID:
                currentToken = reservedLookup(tokenString)
        position += 1
        
    if imprime:
        print(lineno, currentToken," = ", tokenString) # prints a token and its lexeme
    #print("CURRENT:", currentToken, lineno)
    return currentToken, tokenString, lineno

#f = open('prueba.tny', 'r')
##f = open('sample.tny', 'r')
#program = f.read() # lee todo el archivo a compilar
#programLength = len(program) # original program length
#program = program + '$' # add a character to represente EOF
#position = 0 # the position of the current char in file

