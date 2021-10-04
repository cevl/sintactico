import json

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { 'a' : 'id', 'b' : 'id', 'c' : 'id' , 'd' : 'id' }
identifier_key = identifier.keys()

with open('tokens.json', 'r') as openfile:
    program = json.load(openfile)
    
    count = 0
    for line in program:
        count += 1
        print('Line# ', count, '\n')
        
        if(line[-1] not in punctuation_symbol_key):
            print('Error al final de la linea #', count, 'No se usaron los simbolos de puntuación correctos \n')
        if(line[0] not in identifier_key and line[0] not in data_type_key):
            print('Error al principio de la linea #', count, 'No se reconoce la variable o el tipo de datos')
        
        
        