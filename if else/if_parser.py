import ply.yacc as yacc
from if_lexer import tokens

flag=0
def p_ifstmt(p):
    
    '''
    ifstmt :  IF LEFTBRACKET conditions RIGHTBRACKET LEFTBRACE statements RIGHTBRACE
           |  IF LEFTBRACKET conditions RIGHTBRACKET statementSingle
           |  IF LEFTBRACKET conditions RIGHTBRACKET LEFTBRACE statements RIGHTBRACE ELSE LEFTBRACE statements RIGHTBRACE
           |  IF LEFTBRACKET conditions RIGHTBRACKET statements ELSE statements
    '''
    #this works for 
    #case 1: if(a>10){a=11}
    #case 2: if(a>10) a=11
    #case 3: if(a>10){a=11}else{a=10}
    #case 4: if(a>10)a=11 else a=10
    
    if len(p) == 6:
        p[0] = (p[1],p[3],p[5])
    elif len(p)==11:
        p[0] = (p[1],p[3],p[6],p[8],p[10])
    elif len(p)==8 and p[6]=='LEFTBRACE':
        p[0]=(p[1],p[3],p[6])
    else:
        p[0]=(p[1],p[3],p[5],p[6],p[7])

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    if len(p) == 2:
        p[0] = (p[1],)
    else:
        p[0] = p[1]+(p[2],)


def p_statement(p):
    '''
    statement : list 
             | ifstmt
             | empty
    '''
    p[0] = (p[1],) if len(p) == 2 else p[1]

def p_statementSingle(p):
    '''
    statementSingle : ifstmt
                    | list
                    | empty
    '''
    if len(p) == 3:
        p[0] = (p[1],)
    else:
        p[0] = p[1]

def p_list(p):
    '''
    list : ID list 
         | ID
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_conditions(p):
    '''
    conditions  : ID EQUALS ID 
                | ID GREATER ID 
                | ID LESSER ID 
                | ID GREATER EQUALS ID 
                | ID LESSER EQUALS ID 
                | ID NOT EQUALS ID
                | conditions AND conditions 
                | conditions OR conditions
                | ID
    '''
    
    if len(p) == 2:
        p[0] = ('condition',p[1])
    else:
        p[0] = ('condition',(p[1],p[2],p[3]))

def p_error(p):
    print("Syntax error")
    global flag
    flag = 1




parser=yacc.yacc()



while True:
    flag=0
    try:
        s=input('enter the declaration:')
    except EOFError:
        break
    if not s:
        flag=0
        continue
    result=parser.parse(s)
    if flag==0:
        print("Result:",result)
        print("VALID SYNTAX")
