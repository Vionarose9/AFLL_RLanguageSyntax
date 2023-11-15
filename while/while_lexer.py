import ply.lex as lex
tokens = ('WHILE',
        'LBRACKET','RBRACKET',
        'LESSER',
        'GREATER',
        'NOT',
        'AND',
        'OR',
        'EQUALS',
        'LFLOWER',
        'RFLOWER',
        'ID','ARROW')

#Defining token rules
t_LBRACKET = r'\('
t_RBRACKET = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'
def t_WHILE(t):
    r'while'
    return t
def t_ID(t):
    r'\b([a-zA-Z_=][a-zA-Z_0-9]*)\b |\b(\d+)\b'
    return t
def t_ARROW(t):
    r'\<-'
    return t
t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'=(=)?'
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_ignore = ' \t'

#Incase of error
def t_error(t):
    print(f"Illegal character found {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex.lex()
data = input()
lexer.input(data)
while(1):
    tok = lexer.token()
    if not tok:
        break
    print(tok)