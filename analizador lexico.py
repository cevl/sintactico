import json

file = open("read.py")

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'int' : 'integer type', 'float': 'Floating point' , 'char' : 'Character type', 'long' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { 'a' : 'id', 'b' : 'id', 'c' : 'id' , 'd' : 'id' }
identifier_key = identifier.keys()


a=file.read()

count=0
program = a.split("\n")
jprogram = []
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    jtokens = []
    for token in tokens:
        if token in operators_key:
            print("operator is ", operators[token])
            jtokens.append(token)
        if token in data_type_key:
            print("datatype is", data_type[token])
            jtokens.append(token)
        if token in punctuation_symbol_key:
            print (token, "Punctuation symbol is" , punctuation_symbol[token])
            jtokens.append(token)
        if token in identifier_key:
            print (token, "Identifier is" , identifier[token])
            jtokens.append(token)
    
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 
    jprogram.append(jtokens);
json_object = json.dumps(jprogram, indent = 4)
with open("tokens.json", "w") as outfile:
    outfile.write(json_object)