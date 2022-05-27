def check_string(state,char):
    match state:
        case '1':
            if(char== "ID"):
                state = '2'
                return state
            elif(char=="Num"):
                state = '3'
                return state
            elif(char in '+-*/'):
                state = 'error'
                return state

            elif (char == '('):
                state = '1'
                return state

            elif (char == ')'):
                state = '1'
                return state

            elif (char.isspace()):
                state = '1'
                return state
            else:
                state = 'error'

                return state
        case '2':
            if (char== "ID" ):
                state = 'error'

                return state
            elif (char == "Num"):
                state = '2'

                return state
            elif (char == '('):
                state = '2'
                return state

            elif (char == ')'):
                state = '2'
                return state

            elif (char in '+-*/'):
                state = '4'
                return '4'
            elif (char.isspace()):
                state = '2'
                return state
            else:
                state = 'error'

                return state
        case '3':
            if (char == "ID" ):
                state = 'error'

                return state
            elif (char == "Num"):
                state = 'error'

                return state
            elif (char in '+-*/'):
                state = '4'

                return state
            elif (char.isspace()):
                state = '3'
                return state

            elif (char == '('):
                state = '3'
                return state

            elif (char == ')'):
                state = '3'
                return state


            else:
                state = 'error'

                return state
        case '4':
            if (char == "ID"):
                state = '5'

                return state
            elif (char == "Num"):
                state = '6'
                return '6'
            elif (char in '+-*/'):
                state = 'error'

                return state

            elif (char == '('):
                state = '4'
                return state

            elif (char == ')'):
                state = '4'
                return state

            elif (char.isspace()):
                state = '4'
                return state
            else:
                state = 'error'
                return state
        case '5':
            if (char == "ID"):
                state = 'error'
                return state
            elif (char == "Num"):
                state = 'error'
                return state
            elif (char in '+-*/'):
                state = '4'
                return state

            elif (char == '('):
                state = '5'
                return state

            elif (char == ')'):
                state = '5'
                return state

            elif (char.isspace()):
                state = '5'
                return state
            else:
                state = 'error'
                return state
        case '6':
            if (char == "ID"):
                state = 'error'

                return state
            elif (char == "Num"):
                state = 'error'

                return state

            elif (char in '+-*/'):
                state = '4'
                return state

            elif (char.isspace()):
                state = '6'
                return state

            elif (char=='('):
                state = '6'
                return state

            elif (char==')'):
                state = '6'
                return state

            else:
                state = 'error'
                return state
        case 'error':
            state='error'
            return 'error'


def check_expression(letter,l,toks):
    state='1'
    st = letter.split()

    for word in st:
        if (word[0].isalpha()):
            l.append(str('< ' + word +' , ' + 'ID >'))
            toks.append('ID')
        elif(word == '('):
            l.append(str('< ' +word +' , '+ '"(" >'))
            toks.append('(')
        elif(word == ')'):
            l.append(str('< ' +word +' , ' + '")" >'))
            toks.append(")")
        elif(word.isnumeric()):
            l.append(str('< ' + word + ' , ' + 'Num >'))
            toks.append("Num")
        elif(word[0] == '+'):
            l.append(str('< ' +word +' , '+  'operator >'))
            toks.append('+')
        elif (word[0] == '*'):
            l.append(str('< ' + word + ' , ' + 'operator >'))
            toks.append('*')
        elif (word[0] == '-'):
            l.append(str('< ' + word + ' , ' + 'operator >'))
            toks.append('-')
        elif (word[0] == '/'):
            l.append(str('< ' + word + ' , ' + 'operator >'))
            toks.append('/')
        else:
            toks.clear()
            toks.append("error")
            l.append(str('< ' + word + ' , ' + 'error >'))
            break
    for i in (toks):
        state = check_string(state, i)
    print(state)
    if (not(state == "6") and not(state=="5") )or state == 'error':
        toks.clear()
        toks.append("error")
        l.append("error")
    toks.append("$")


def add_spaces(letter, y):
    for i in letter:
        if i == "+" or i == "-" or i == "(" or i == ")" or i == "*" or i == "/":
            y.append(" ")
            y.append(i)
            y.append(" ")
        else:
            y.append(i)
    letter = ""
    for j in y:
        letter = letter + j
    return letter

"""t=[]
check_expression("2 + ( ( z ) )",[],t)

for i in t:
    print(i)

"""