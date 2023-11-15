from enum import Enum

def eval(lisp):

    ''' 
    Calculate floor from a string with a LISP Code. 
    '''

    # Lee la cadena de caracteres
    characters = read(lisp)
 
    # Calcular el piso
    floor = 0
    for char in characters:
        
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        else:
            floor = floor

    return floor



def read(string):

    ''' 
    Check a string valid and clean of whitespaces, return a new string. 
    '''
    new_string = ""
    # comprueba que la string pasada as válida
    # Captura el error SyntaxisError y devuelve un mensaje del mismo
    #try:
    if check(string):
    # si es valida limpia la string de spacios en blancos
        new_string = parse(string)
    #except SyntaxError as error:
        #print(f'Your string is not valid: {error}')

    
    
    return new_string

def parse(string):
    ''' 
    receives a string and cleans it of whitespace. 
    '''
    clean_string = ""

    for char in string:
        if char in (")("):
            clean_string = clean_string + char
    return clean_string

def check(string):
    ''' 
    Return True when all string only have parenthesis and whitespaces.
    Raise a SyntaxError in other cases with a message with position and char.
    '''
    valid_string = True
    for char in string:
        if char in "() \r\n\t":
            valid_string = True
        else:
            index = string.index(char)
            raise SyntaxError(f'{char} in {index} position is not a allowed parameter.')
          
        
    return valid_string




def eval_rpl():
    ''' 
    Infinte while bucle.
    User introduce a LISP Code as string or quit. 
    When raise a SyntaxErro return a massage. 
    '''


    class UserChoice(Enum):
        LISP = 0
        QUIT = 1

    while True:
        print(f"{UserChoice.LISP.value}. I want add a LISP CODE")
        print(f'{UserChoice.QUIT.value}. I want exit')
        print("***************************************")
        answer = int(input('Enter your option: '))

        if answer == 0:
            new_string = input("Introduce your LISP code: ")

            try: 
                floor = eval(new_string)
                print(f"your floor is {floor}\n")
            except SyntaxError as err:
                print(f'{err}\n')
        else:
            break
        

    pass

if __name__== "__main__":
    eval_rpl()

