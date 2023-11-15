import ply.lex as lex
tokens = ('FOR',
        'LBRACE',
        'COLON',
        'IN',
        'RBRACE',
        'LFLOWER',
        'RFLOWER',
        'ID',
        'NUM',
        )

def t_FOR(t):
    r'for'
    return t
def t_IN(t):
    r'in'
    return t

t_LBRACE = r'\('
t_RBRACE = r'\)'
t_LFLOWER = r'\{'
t_RFLOWER = r'\}'

def t_COLON(t):
    r'\:'
    return t
def t_ID(t):
    r'\b([a-zA-Z_=][a-zA-Z_0-9]*)\b'
    return t
def t_NUM(t):
    r'[0-9][0-9]*'
    return t

t_ignore = ' \t'

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